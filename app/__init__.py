from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_mail import Mail
from .models import db, User
from .routes import main as main_blueprint
from .auth import auth as auth_blueprint
from flask import render_template

mail = Mail()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mail.init_app(app)
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Create database tables if needed
    with app.app_context():
        from . import models
        db.create_all()
    
    @app.errorhandler(404)
    def not_found_error(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(e):
        from .models import db
        db.session.rollback()
        return render_template('errors/500.html'), 500



    # Register blueprints after app and extensions are ready
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app

