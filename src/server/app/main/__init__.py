""" Creation of Flask object along with configuration based on environment name specified in the settings file"""
import logging
from datetime import datetime as dt
from flask import Flask, Blueprint, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_jwt_extended import JWTManager

from .settings import config_by_name
from app.main.utils.LogSetup import LogSetup

logs = LogSetup()
db = SQLAlchemy()
admin = Admin()
flask_bcrypt = Bcrypt()
login_manager = LoginManager()
flask_jwt_manager = JWTManager()
api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)


def create_app(config_name):
    """
    creates the Flask object

    Args:
        config_name (str): string to define the environment settings the Flask object will be configured with

    Returns:
        object: Flask object configured with the configuration parameters from settings based on the environment name specified
    """
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    add_extentions(app=app)


    @app.after_request
    def after_request(response):
        """ Logging after every request. """
        logger = logging.getLogger("app.access")
        logger.info(
            "%s [%s] %s %s %s %s %s %s %s",
            request.remote_addr,
            dt.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
            request.method,
            request.path,
            request.scheme,
            response.status,
            response.content_length,
            request.referrer,
            request.user_agent,
        )
        return response

    return app

def add_extentions(app):
    # api.init_app(app)
    db.init_app(app)
    logs.init_app(app)
    flask_bcrypt.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    flask_jwt_manager.init_app(app)
    