from flask import Response

def throw(_message):
    message = _message if _message is str else _message.args[0]

    return Response('{ "message": "' + message + '" }', status=403, mimetype='application/json')
