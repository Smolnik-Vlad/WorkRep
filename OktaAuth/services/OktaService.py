import requests

from djangoProject.settings import OKTA_DOMAIN, CLIENT_SECRET_USER_AUTH, CLIENT_ID_USER_AUTH


class OktaService:
    def __init__(self):
        self.okta_domain = OKTA_DOMAIN
        self.client_id = CLIENT_ID_USER_AUTH
        self.client_secret = CLIENT_SECRET_USER_AUTH

    def get_session_token_for_user(self, username, password):
        url = f"https://{self.okta_domain}/api/v1/authn"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        payload = {
            "username": username,
            "password": password,
            "options": {
                "multiOptionalFactorEnroll": False,
                "warnBeforePasswordExpired": False
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def get_bearer_token_for_user(self, username, password):  # need to use special type of Okta API
        token_url = f'https://{self.okta_domain}/oauth2/default/v1/token'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        token_data = {
            'grant_type': 'password',
            'scope': 'openid',
            'username': username,
            'password': password,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        response = requests.post(token_url, headers=headers, data=token_data)
        return response.json()