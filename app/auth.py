import functools
import re
import json

from sanic.request import Request
from sanic.log import logger

import jwt

from app.response_func import unauthorized, invalid_token


def auth_required(func):
    """can only be used after @app.METHOD decorator where app is a sonic app"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request: Request = args[0]

        # checking for Authorization header
        token_header = request.headers.get('Authorization')
        if token_header is None:
            return unauthorized()

        # extracting token from the header
        token_match = re.compile(r'Bearer (.*)').search(token_header)
        if not token_match:
            return unauthorized()
        token = token_match.group(1)
        secret, hash_algo = request.app.config['SECRET'], request.app.config['JWT_HASH_ALGO']

        # decoding the token
        try:
            payload = jwt.decode(token, secret, algorithms=[hash_algo])
        except jwt.exceptions.InvalidTokenError:
            return invalid_token()

        username, password = payload.get('username'), payload.get('password')
        if username is None or password is None:
            return invalid_token()

        if not validate_user_password(request.app.config['PASSWORD_FILE'], username, password):
            return invalid_token()

        # if reached to this point, the user is authorized
        return func(*args, **kwargs)
    return wrapper


def validate_user_password(path, username, accepted_password):
    """retrive the user password from local passwords file
    if user does not exist return None"""

    # if any exception is raised from this function, then it is an internal server error

    try:
        with open(path, 'r') as file:
            password = json.load(file).get(username)

        if accepted_password != password:
            return False
        else:
            return True
    except FileNotFoundError:
        logger.error('password file was not found')
        raise
    except PermissionError:
        logger.error('no permission to read password file')
        raise
    except json.JSONDecodeError:
        logger.error('password file is not a json file')
        raise
