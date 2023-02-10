from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt = Bcrypt()


login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('main/settings.py')
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from basa.main.routes import main
    from basa.user.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)
    return app

