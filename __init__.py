from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .auth import auth as auth_blueprint
from .main import main as main_blueprint
from .models import User

# initializing the db
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '42'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes (login page (/login) and the sign-up page (/sign-up) and /logout)
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth routes (a home page (/) and profile page (/profile) for after we log in)
    app.register_blueprint(main_blueprint)

    return app


