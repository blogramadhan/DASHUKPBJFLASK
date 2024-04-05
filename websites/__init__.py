from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "SIRUP"

    from .home import home
    from .sirup import sirup
    from .spse import spse
    from .epurchasing import epurchasing
    from .monitoring import monitoring

    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(sirup, url_prefix="/")
    app.register_blueprint(spse, url_prefix="/")
    app.register_blueprint(epurchasing, url_prefix="/")
    app.register_blueprint(monitoring, url_prefix="/")

    return app