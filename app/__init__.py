import jwt
from sanic.response import json as sanic_json
from sanic import Sanic

from app.auth import auth_required, validate_user_password

from app import config
from app.response_func import invalid_body, invalid_credentials, missing_credentials
from app.auth import auth_required


app = Sanic(__name__)
app.update_config(config)


@app.post("/auth")
def auth(request):

    body = request.json
    if not isinstance(body, dict):
        return invalid_body()

    username, password = body.get('username'), body.get('password')
    if username is None or password is None:
        return missing_credentials()

    if not validate_user_password(request.app.config['PASSWORD_FILE'], username, password):
        return invalid_credentials()

    secret, hash_algo = request.app.config['SECRET'], request.app.config['JWT_HASH_ALGO']

    token = jwt.encode(
        {'username': username, 'password': password},
        secret,
        algorithm=hash_algo
    )
    return sanic_json(
        {'token': token.decode('utf-8')},  # decoding to a string
        status=200
    )


@app.post('/norm')
@auth_required
def norm(request):
    body = request.json

    response = {obj['name']: obj[list(filter(lambda x: 'Val' in x, obj.keys()))[0]] for obj in body}
    return sanic_json(response, status=200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)