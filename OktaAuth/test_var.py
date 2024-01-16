import base64

import requests

"""
Functions just for testing
"""


def get_session_token_for_user(username, password, okta_domain):
    url = f"https://{okta_domain}/api/v1/authn"
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


def get_access_token_for_api(client_id, client_secret, okta_domain):
    token_url = f'https://{okta_domain}/oauth2/default/v1/token'

    client_credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(client_credentials.encode('utf-8')).decode('utf-8')

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {encoded_credentials}'
    }

    token_data = {
        'grant_type': 'client_credentials',
        'scope': 'zartico_scope'
    }

    response = requests.post(token_url, headers=headers, data=token_data)
    return response.json()


def get_bearer_token_for_user(username, password, client_id, client_secret):
    token_url = f'https://dev-92454775.okta.com/oauth2/default/v1/token'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    token_data = {
        'grant_type': 'password',
        'scope': 'openid',
        'username': username,
        'password': password,
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(token_url, headers=headers, data=token_data)
