from flask import request
from flask_restful import Resource
from ..services.user_service import save_new_user, get_all_users
import requests
from app.main.services.auth_service import Auth
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
        post_data = request.json
        return Auth.login_user(data=post_data)


class LogoutAPI(Resource):
    """
    Logout Resource
    """

    def post(self):
        # get auth token
        auth_header = request.headers.get("Authorization")
        return Auth.logout_user(data=auth_header)


class GithubAuthorize(Resource):
    @classmethod
    def post(cls):
        data = request.json
        code = data.get("code")
        url = "https://github.com/login/oauth/access_token"
        my_data = {
            "code": code,
            "client_id": "c1d53a4b044962c3379a",
            "client_secret": "a2b7acacd1b94dde26fc1dae18b8c6e7f9e1f22f",
        }
        x = requests.post(
            url, data=my_data, headers={"Accept": "application/json"}
        )
        data = x.json()
        g.access_token = data["access_token"]
        # github_user_data = dict(username=github.get("login"))
        github_user = github.get("user")
        github_email = github.get("user/emails")
        github_new_user = dict(
            username=github_user.data.get("login"),
            name=github_user.data.get("name")
            if github_user.data.get("name")
            else github_user.data.get("login"),
            email=github_email.data[0].get("email"),
        )
        return save_new_user(github_new_user)


class FacebookAuthorize(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        access_token = data["access_token"]
        g.facebook_access_token = access_token
        facebook_user = facebook.get("me?fields=id,name,email").data
        user_data = dict(
            username=facebook_user["id"],
            name=facebook_user["name"],
            email=facebook_user["email"],
        )
        return save_new_user(data=user_data)
