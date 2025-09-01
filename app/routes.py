from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from functools import wraps

# Create the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')  # Ensure this template exists

@main.route('/home')
def home_redirect():
    return redirect(url_for('main.index'))

# Role-based access decorator
def role_required(roles):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                flash("Permission denied", "warning")
                return redirect(url_for('main.index'))
            return f(*args, **kwargs)
        return wrapped
    return decorator

@main.route('/incidents')
@login_required
def list_incidents():
    from .models import Incident
    incidents = Incident.query.all()
    return render_template('incidents/list.html', incidents=incidents)

@main.route('/incidents/new', methods=['GET', 'POST'])
@login_required
@role_required(['reporter', 'admin'])
def create_incident():
    from .forms import IncidentForm
    from .models import Incident, User, db
    from .emails import send_email

    form = IncidentForm()
    if form.validate_on_submit():
        new_inc = Incident(title=form.title.data, description=form.description.data)
        db.session.add(new_inc)
        db.session.commit()

        # === Notify Admins ===
        admins = [u.email for u in User.query.filter_by(role='admin').all() if u.email]
        if admins:
            send_email(
                subject=f"New Incident Created: {new_inc.title}",
                recipients=admins,
                text_body=f"A new incident \"{new_inc.title}\" has been reported.\n\nDescription: {new_inc.description}",
                html_body=render_template('email/new_incident.html', incident=new_inc)
            )
        # =====================

        flash('Incident created!', 'success')
        return redirect(url_for('main.list_incidents'))

    return render_template('incidents/new.html', form=form)

@main.route('/incidents/<int:incident_id>')
@login_required
def view_incident(incident_id):
    from .models import Incident
    inc = Incident.query.get_or_404(incident_id)
    return render_template('incidents/view.html', incident=inc)

@main.route('/incidents/<int:incident_id>/edit', methods=['GET', 'POST'])
@login_required
@role_required(['engineer', 'admin'])
def edit_incident(incident_id):
    from .forms import AssignIncidentForm
    from .models import Incident, User, db
    from .emails import send_email

    inc = Incident.query.get_or_404(incident_id)
    form = AssignIncidentForm(obj=inc)

    # Populate dropdown with engineers
    form.assigned_to.choices = [(u.id, u.username) for u in User.query.filter_by(role='engineer').all()]

    if form.validate_on_submit():
        old_status = inc.status
        old_assignee = inc.assigned_to_id

        inc.assigned_to_id = form.assigned_to.data
        inc.status = form.status.data
        db.session.commit()

        # === Notify Admins ===
        admins = [u.email for u in User.query.filter_by(role='admin').all() if u.email]

        # Assigned to Engineer
        if inc.assigned_to_id and inc.assigned_to_id != old_assignee:
            engineer = User.query.get(inc.assigned_to_id)

            # Notify Admins
            if admins:
                send_email(
                    subject=f"Incident Assigned: {inc.title}",
                    recipients=admins,
                    text_body=f"The incident \"{inc.title}\" has been assigned to engineer {engineer.username}.",
                    html_body=render_template('email/incident_assigned.html', incident=inc, engineer=engineer)
                )

            # Notify Engineer
            if engineer and engineer.email:
                send_email(
                    subject=f"You have been assigned an Incident: {inc.title}",
                    recipients=[engineer.email],
                    text_body=f"You have been assigned the incident \"{inc.title}\". Please check the system for details.",
                    html_body=render_template('email/incident_assigned_engineer.html', incident=inc, engineer=engineer)
                )

        # Resolved
        if inc.status == 'resolved' and old_status != 'resolved':
            if admins:
                send_email(
                    subject=f"Incident Resolved: {inc.title}",
                    recipients=admins,
                    text_body=f"The incident \"{inc.title}\" has been resolved.",
                    html_body=render_template('email/incident_resolved.html', incident=inc)
                )

        flash('Incident updated!', 'success')
        return redirect(url_for('main.view_incident', incident_id=inc.id))

    return render_template('incidents/edit.html', form=form, incident=inc)

@main.route('/incidents/<int:incident_id>/delete', methods=['POST'])
@login_required
@role_required(['admin'])
def delete_incident(incident_id):
    from .models import Incident, db

    inc = Incident.query.get_or_404(incident_id)
    db.session.delete(inc)
    db.session.commit()
    flash('Incident deleted.', 'info')
    return redirect(url_for('main.list_incidents'))

# Insert into your routes.py
@main.route('/test-email')
def test_email():
    from .emails import send_email
    import os
    send_email(
        subject='Test Email',
        recipients=[os.environ.get('EMAIL_USER')],
        text_body='This is a test.',
        html_body='<p>This is a <strong>test</strong>.</p>'
    )
    return "Sent test email!"
