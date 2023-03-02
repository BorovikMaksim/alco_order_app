from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy(session_options={"autoflush": False})
bcrypt = Bcrypt()
migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Авторизуйтесь, чтобы попасть на эту страницу!'

from basa import models


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('main/settings.py')
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db, render_as_bath=True, compare_type=True)

    from basa.main.routes import main
    from basa.user.routes import users
    from basa.order.routes import orders

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(orders)

    return app
