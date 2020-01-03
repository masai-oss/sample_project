# Back-end Guide

## Requirements
1. Setup the database server based on the project requirement

### After cloning follow the steps to setup

1. Create virtual environment with `pipenv/virtualenv` for python version 3.7.3 (or higher)
2. Activate the virtual environment `source <virtual_environment_name>/bin/activate`
3. `pip install -r requirements.txt`

### To start the server
``` python manage.py run ```



### To add the models

1. Create {model}.py files in the models folder

   Example

   ```python
   # in app.main.models
   from app.main import db
   class User(db.Model):
       """
       [summary]
       
       Args:
           UserMixin ([type]): [description]
           db ([type]): [description]
       """
       __tablename__ = "users"
   
       id = db.Column(db.Integer, primary_key=True)
       public_id = db.Column(db.String(50), unique=True)
       username = db.Column(db.String(30), unique=True, nullable=False)
       email = db.Column(db.String(100), unique=True, nullable=False)
       name = db.Column(db.String(150), nullable=False)
       admin = db.Column(db.Boolean, nullable=False, default=False)
       password_hash = db.Column(db.String(100))
   ```

2. import the same file in the `models/__init__.py` 

   ##### Example

   ```python
   """ import all the models in the folder here"""
   from app.main.models.user import User
   ```

3. run the db migrate and upgrade command again

### To migrate the database

##### To change the DB settings

1. Create data-base in respective server
2. Open the `settings.py` in the root folder
3. Change the database URI in `SQLALCHEMY_DATABASE_URI` based on the development env

##### To create migrations folder

1. `python manage.py db init`

##### To make the migrations

1. `python manage.py db stamp head`
2. `python manage.py migrate`
3. `python manage.py db upgrade`
4. make a migration every time you make a change to the models

P.S: To make the migrations easier use `make migrate` command


### To create the routes
1. Create the {route}.py file in the route folder 

   ##### Example

   ```python
   #flask-restful
   from flask import request
   from flask_restful import Resource
   from ..services.user_service import save_new_user, get_all_users
   import requests
   from app.main.services.auth_helper import Auth
   from app.main.utils.oauth_utils import github, oauth, facebook, g
   
   class UserSignUp(Resource):
       """
       [summary]
       
       Args:
           Resource ([type]): [description]
       """
       def post(self):
           """Creates a new User """
           data = request.json
           return save_new_user(data=data)
   
   
   class UserLogin(Resource):
       """
           User Login Resource
       """
       def post(self):
           # get the post data
           post_data = request.json
           return Auth.login_user(data=post_data)
   ```

   ##### Example

   ```python
   # blueprint
   from flask import Blueprint, current_app
   
   bp = Blueprint("public", __name__)
   
   @bp.route("/hw")
   def hello_world():
       current_app.logger.info("Here I am")
       current_app.logger.warning(" Warning you")
       current_app.logger.error("But you can't hear me")
   
       return "hello hello_world"
   ```

   

2. import the file into `routes/__init__.py`

3. if the routes are blueprint then register the blueprint under 'register_blueprints' function in the init.py files

4. if the routes are flask RESTful, api.add_resource({RESTful_name}, '{route}')

   ##### Example

   ```python
   from app.main.routes.auth_controller import UserLogin, LogoutAPI, UserSignUp, FacebookAuthorize, GithubAuthorize
   from app.main import api
   from app.main.routesblueprint_test import bp
   
   def add_resources(app):
       """
       Method to add resources to app context
       
       Args:
           app (object): object of Flask representing the app in context
       """
       api.add_resource(UserLogin, '/login')
       api.add_resource(LogoutAPI, '/logout')
       api.add_resource(UserSignUp, '/signup')
       api.add_resource(FacebookAuthorize, '/facebook')
       api.add_resource(GithubAuthorize, '/github')
   
   def register_blueprints(app):
       """
       Method to add blueprints to app context
       
       Args:
           app (object): object of Flask representing the app in context
       """
       app.register_blueprint(bp)
   ```

   

   

### To create the services
Add any interaction with data and models into the services folder

##### Example

```python
@login_manager.user_loader
def load_user(user_id):
    """
    [summary]
    
    Args:
        user_id ([type]): [description]
    
    Returns:
        [type]: [description]
    """
    return User.query.get(int(user_id))

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            name=data['name'],
            admin=data.get('admin', False),
            password=data.get('password', None)
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()
```



### To create the utility functionality
Add the utility functions in the 'utils' folder.

##### Example

```python
from flask_oauthlib.client import OAuth
from flask import g
oauth = OAuth()

github = oauth.remote_app('github',
                          consumer_key="c1d53a4b044962c3379a",
                          consumer_secret="a2b7acacd1b94dde26fc1dae18b8c6e7f9e1f22f",
                          request_token_params={"scope": "user:email"},
                          base_url="https://api.github.com/",
                          request_token_url=None,
                          request_token_method="POST",
                          access_token_url="https://github.com/login/oauth/access_token",
                          authorize_url="https://github.com/login/oauth/authorize"
                          )


@github.tokengetter
def get_github_token():
    if 'access_token' in g:
        return g.access_token

```
### To use OAuth in the application

Add the required tokens/credentials as specified under `SECRET_KEYS` in `settings.py` to environment variables.


### To create logs
1. import current_app from flask

2. log messages based on the level of logs

   ##### Example

   ```python
   from flask import Blueprint, current_app
   
   bp = Blueprint("public", __name__)
   
   @bp.route("/hw")
   def hello_world():
       current_app.logger.info("Here I am")
       current_app.logger.warning(" Warning you")
       current_app.logger.error("But you can't hear me")
   
       return "hello hello_world"
   ```

3. Check for the logs in `/tmp/app.log` file they should be in the following format:

   ##### Example

   ```
   [30/Dec/2019:18:24:13.295] INFO werkzeug:_log:  * Restarting with stat
   [30/Dec/2019:18:24:13.981] WARNING werkzeug:_log:  * Debugger is active!
   [30/Dec/2019:18:24:13.987] INFO werkzeug:_log:  * Debugger PIN: 232-702-839
   [30/Dec/2019:18:27:16.397] INFO werkzeug:_log:  * Detected change in '/home/masai/flask_boilerplate/app/main/models/user.py', reloading
   [30/Dec/2019:18:27:16.495] INFO werkzeug:_log:  * Restarting with stat
   [30/Dec/2019:18:27:16.987] WARNING werkzeug:_log:  * Debugger is active!
   [30/Dec/2019:18:27:16.994] INFO werkzeug:_log:  * Debugger PIN: 232-702-839
   [30/Dec/2019:18:27:43.058] INFO werkzeug:_log: 127.0.0.1 - - [30/Dec/2019 18:27:43] "POST /login HTTP/1.1" 200 -
   [30/Dec/2019:18:32:03.248] INFO werkzeug:_log:  * Detected change in '/home/masai/flask_boilerplate/app/main/services/auth_helper.py', reloading
   [30/Dec/2019:18:32:03.335] INFO werkzeug:_log:  * Restarting with stat
   [30/Dec/2019:18:32:03.667] WARNING werkzeug:_log:  * Debugger is active!
   [30/Dec/2019:18:32:03.672] INFO werkzeug:_log:  * Debugger PIN: 232-702-839
   [30/Dec/2019:18:32:32.172] INFO werkzeug:_log:  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   [30/Dec/2019:18:32:32.173] INFO werkzeug:_log:  * Restarting with stat
   [30/Dec/2019:18:32:32.480] WARNING werkzeug:_log:  * Debugger is active!
   [30/Dec/2019:18:32:32.486] INFO werkzeug:_log:  * Debugger PIN: 232-702-839
   [30/Dec/2019:18:32:38.760] INFO werkzeug:_log: 127.0.0.1 - - [30/Dec/2019 18:32:38] "POST /login HTTP/1.1" 200 -
   [30/Dec/2019:18:32:44.770] INFO werkzeug:_log: 127.0.0.1 - - [30/Dec/2019 18:32:44] "POST /logout HTTP/1.1" 403 -
   [30/Dec/2019:18:32:51.078] INFO werkzeug:_log: 127.0.0.1 - - [30/Dec/2019 18:32:51] "POST /login HTTP/1.1" 200 -
   [30/Dec/2019:18:34:07.440] INFO werkzeug:_log: 127.0.0.1 - - [30/Dec/2019 18:34:07] "POST /logout HTTP/1.1" 500 -
   [30/Dec/2019:18:35:08.874] INFO werkzeug:_log:  * Detected change in '/home/masai/flask_boilerplate/app/main/services/auth_helper.py', reload
   ```

   
### Few things to keep in mind

1. Run the command `make clean`to clear out all the `__pycache__` folders and files, before you psuh files to github

2. Follow `pep8` rules to avoid commit issues including the docstrings in google format

   Example for methods:

   ```python
     """method to add todo to the model Todo
       Args:
           data (dict): data which needs to be stored into Todo table
                       using Todo model
       Returns:
           dict: response object containing appropriate response based on the 						response from save changes,
           int: http response code specifying the success or failure of storing data into 				table
       """
   ```

   

   Example for classes:

      ```python
 """SQLAlchemy model for Todo items
    containing fileds id and todo_item 
    id: unique identifier
    todo_item: the todo item to be added to the database
    Args:
        db (object): SQLAlchemy object imported from main 
    """
      ```

3. Add docstrings to the file to describe the function of the file in brief
4. Add your static files to `server/src/app/main/static` folder