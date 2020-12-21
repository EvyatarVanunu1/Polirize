from sanic.response import json as sanic_json


def invalid_body():
    return sanic_json(
        {
            'msg': 'invalid body',
            'details': 'body should be a json object'
         },
        status=401
    )


def unauthorized():
    return sanic_json(
        {
            'msg': 'unauthorized',
            'details': 'missing Bearer token in headers'
         },
        status=401
    )


def invalid_token():
    return sanic_json(
        {
            'msg': 'invalid token',
            'details': ''
         },
        status=401
    )


def invalid_credentials():
    return sanic_json(
        {
            'msg': 'invalid password or username',
            'details': ''
         },
        status=401
    )


def missing_credentials():
    return sanic_json(
        {
            'msg': 'missing password or username',
            'details': ''
         },
        status=401
    )

