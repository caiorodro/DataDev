from flask import Flask
from app.routeTemplates import dataTemplate
from app.routeFilters import dataFilter
from app.routeFiles import dataFile
from app.routeUsers import dataUser
from app.routeQueries import dataQuery
import os
# import logging
# import graypy
# from werkzeug.exceptions import HTTPException, default_exceptions

cwd = os.getcwd()

templates = '/'.join((cwd, 'app/templates/'))
app = Flask(__name__, template_folder=templates, static_url_path="")

packs = [dataTemplate, dataFilter, dataFile, dataUser, dataQuery]

[app.register_blueprint(pack) for pack in packs]

# def error_handling(error):
#     if isinstance(error, HTTPException):
#         result = {'code': error.code, 'description': error.description}
#     else:
#         description = default_exceptions[500].description
#         result = {'code': 500, 'description': description}

#     app.logger.exception(str(error), extra=result)
#     result['message'] = str(error)
#     resp = jsonify(result)
#     resp.status_code = result['code']
#     return resp

# for code in default_exceptions.keys():
#     app.register_error_handler(code, error_handling)

if __name__ == '__main__':
    app.run()
    # handler = graypy.GELFHTTPHandler('localhost', 12201)
    # app.logger.addHandler(handler)
