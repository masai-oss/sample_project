# import resprctive blueprints and flask REstful resources
from .blueprint_test import bp

def add_resources(app):
    """
    Method to add resources to app context
    
    Args:
        app (object): object of Flask representing the app in context
    """
    pass

def register_blueprints(app):
    """
    Method to add blueprints to app context
    
    Args:
        app (object): object of Flask representing the app in context
    """
    app.register_blueprint(bp)
