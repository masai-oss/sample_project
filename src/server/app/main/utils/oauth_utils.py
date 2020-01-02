from flask_oauthlib.client import OAuth
from flask import g

oauth = OAuth()

github = oauth.remote_app(
    "github",
    consumer_key="c1d53a4b044962c3379a",
    consumer_secret="a2b7acacd1b94dde26fc1dae18b8c6e7f9e1f22f",
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
    consumer_key="795350070968827",
    consumer_secret="8d58a97f5364818cf814fa28df6dfa24",
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
    consumer_key="573768465288-9grunuq6fl5fc38a2sq8e7fkdhk209c2.apps.googleusercontent.com",
    consumer_secret="soxNFgpwtlPGF_P1H-bb8BIT",
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
