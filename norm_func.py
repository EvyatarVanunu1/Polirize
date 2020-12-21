import json


def norm_list(event, context):
    ls = json.loads(event.get('body', '[]'))
    payload = json.dumps({obj['name']: obj[list(filter(lambda x: 'Val' in x, obj.keys()))[0]] for obj in ls})
    return {"statusCode": 200, "body": payload}
