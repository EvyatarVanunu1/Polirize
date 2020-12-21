from sanic.response import json as sanic_json


def response_func(msg, status=200, details=''):
    return sanic_json(
        {
        'msg': msg,
        'details': details
        },
        status=status
    )

