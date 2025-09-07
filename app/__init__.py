from flask import Flask, render_template
from config import Config
from flask_login import LoginManager
from flask_mail import Mail
from .models import db, User
from .routes import main as main_blueprint
from .auth import auth as auth_blueprint
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Gauge

# Initialize extensions
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

# Create a gauge metric
app_up = Gauge('incident_app_up', 'Whether the app is running')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Create database tables if needed
    with app.app_context():
        from . import models
        db.create_all()

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(e):
        db.session.rollback()
        return render_template('errors/500.html'), 500

    # Register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    # Add the /metrics route here
    @app.route('/metrics')
    def metrics():
        app_up.set(1)  # Set to 1 if the app is running
        return generate_latest(app_up), 200, {'Content-Type': CONTENT_TYPE_LATEST}

    return app