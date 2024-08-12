from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['WTF_CSRF_ENABLED'] = True  # Enable CSRF protection

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)  # Initialize CSRF protection

    # Specify the login view so that Flask-Login knows where to redirect users
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'

    from app.models import User  # Import your models here

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(email=user_id).first()


    with app.app_context():
        from . import routes  # Import routes after app context is created
        db.create_all()  # Create database tables

    return app
