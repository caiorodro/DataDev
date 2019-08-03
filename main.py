from flask import Flask
from app.routeTemplates import dataTemplate
from app.routeFilters import dataFilter
from app.routeFiles import dataFile
from app.routeUsers import dataUser
from app.routeQueries import dataQuery
import os

cwd = os.getcwd()

templates = '/'.join((cwd, 'app/templates/'))
app = Flask(__name__, template_folder=templates, static_url_path="")

packs = [dataTemplate, dataFilter, dataFile, dataUser, dataQuery]

[app.register_blueprint(pack) for pack in packs]

if __name__ == '__main__':
    app.run()
