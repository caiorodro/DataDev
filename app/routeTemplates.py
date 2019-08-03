
import os
from flask import Blueprint
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import redirect
from flask import url_for
import json
from app.Usuario import Usuario

from app.Queries import viewData as vd

cwd = os.getcwd()

dataTemplate = Blueprint('dataTemplate', __name__)

@dataTemplate.route('/scripts/<path:path>')
def send_scripts(path):
    return send_from_directory('templates/scripts', path)

@dataTemplate.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)

@dataTemplate.route('/csv/<path:filename>', methods=['GET', 'POST'])
def downloadCSV(filename):
    uploads = '/'.join((cwd, '../csv/'))
    return send_from_directory(directory=uploads, filename=filename)

@dataTemplate.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('templates/assets', path)

@dataTemplate.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('templates/images', path)

@dataTemplate.route('/dist/<path:path>')
def send_dist(path):
    return send_from_directory('templates/dist', path)

@dataTemplate.route("/")
def hello():
    return render_template('painel1.html')

@dataTemplate.route("/panel")
def panel():
    return render_template('painel1.html')

@dataTemplate.route('/recover', methods=['POST', 'GET'])
def recover():
    return render_template('recoverPass.html')

@dataTemplate.route('/toUsuario', methods=['POST', 'GET'])
def toUsuario():
    return render_template('user.html')

@dataTemplate.route('/toUpload', methods=['POST', 'GET'])
def toUpload():
    return render_template('files.html')

@dataTemplate.route('/toPainel', methods=['POST', 'GET'])
def toPainel():
    return render_template('painel.html')
