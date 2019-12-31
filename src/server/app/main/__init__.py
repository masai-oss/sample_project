""" Creation of Flask object along with configuration based on environment name specified in the settings file"""
import logging
from datetime import datetime as dt
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .settings import config_by_name
from app.main.utils.LogSetup import LogSetup

logs = LogSetup()
db = SQLAlchemy()
flask_bcrypt = Bcrypt()


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
    db.init_app(app)
    logs.init_app(app)
    flask_bcrypt.init_app(app)


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