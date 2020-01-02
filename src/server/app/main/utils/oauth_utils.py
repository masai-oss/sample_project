from flask_oauthlib.client import OAuth
from flask import g
from app.main.settings import SECRET_KEYS

oauth = OAuth()

github = oauth.remote_app(
    "github",
    consumer_key=SECRET_KEYS.get("github_consumer_key"),
    consumer_secret=SECRET_KEYS.get("github_consumer_secret"),
    request_token_params={"scope": "user:email"},
    base_url="https://api.github.com/",
    request_token_url=None,
    request_token_method="POST",
    access_token_url="https://github.com/login/oauth/access_token",
    authorize_url="https://github.com/login/oauth/authorize",
)


@github.tokengetter
def get_github_token():
    if "access_token" in g:
        return g.access_token


facebook = oauth.remote_app(
    "facebook",
    consumer_key=SECRET_KEYS.get("facebook_consumer_key"),
    consumer_secret=SECRET_KEYS.get("facebook_consumer_secret"),
    request_token_params={"scope": "public_profile,email"},
    base_url="https://graph.facebook.com/",
    request_token_url=None,
    request_token_method="POST",
    access_token_url="/oauth/access_token",
    authorize_url="https://www.facebook.com/dialog/oauth",
)


@facebook.tokengetter
def get_facebook_token():
    if "facebook_access_token" in g:
        return g.facebook_access_token


google = oauth.remote_app(
    "google",
    consumer_key=SECRET_KEYS.get("google_consumer_key"),
    consumer_secret=SECRET_KEYS.get("google_consumer_secret"),
    request_token_params="",
    base_url="",
    request_token_url=None,
    request_token_method="POST",
    access_token_url="",
    authorize_url="",
)


@google.tokengetter
def get_google_token():
    if "google_access_token" in g:
        return g.google_access_token
