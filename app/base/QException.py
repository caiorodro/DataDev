from flask import Response

def throw(_message):
    message = _message if isinstance(_message, str) else _message.args[0]

    return Response('{ "message": "' + message + '" }', status=403, mimetype='application/json')
