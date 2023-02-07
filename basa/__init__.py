from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask





db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config.from_pyfile('main/settings.py')
    db.init_app(app)
    bcrypt.init_app(app)


    from basa.main.routes import main
    from basa.user.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)
    return app


def login_manager():
    return None