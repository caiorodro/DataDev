
import os
from flask import Blueprint
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import redirect
from flask import url_for
import json
from app.File import File
from app.Queries import viewData as vd

cwd = os.getcwd()

dataFile = Blueprint('dataFile', __name__)

@dataFile.route('/carregaFiles', methods=['POST'])
def carregaFiles():
    rec = json.loads(request.get_data())

    keep = rec['keep']

    file = File(keep)
    result = file.carregaFiles()
    del file

    return result

@dataFile.route('/doUpload', methods=['POST'])
def doUpload():
    file = request.files['UploadedFile']

    content = file.read()

    dataFile = File()
    retorno = dataFile.gravaArquivoNaBase(file.filename, content)
    del dataFile

    return retorno

@dataFile.route('/deletaFile', methods=['POST'])
def deletaFile():
    rec = json.loads(request.get_data())

    idFile = rec['ID_FILE']
    keep = rec['keep']

    file = File(keep)
    file.deletaFile(idFile)

    return "Ok"

@dataFile.route('/downloadContent', methods=['POST'])
def downloadContent():
    rec = json.loads(request.get_data())

    idFile = rec['ID_FILE']
    keep = rec['keep']
    idUsuario = rec['sys']

    file = File(keep)

    pathName = '/'.join((dataFile.root_path[0: dataFile.root_path[0:-1].rfind('/')], 'csv'))

    content = file.downloadContent(idFile, pathName, idUsuario)

    return content

@dataFile.route('/downloadData', methods=['POST'])
def downloadData():
    rec = json.loads(request.get_data())

    table = rec['table']
    keep = rec['keep']
    ANO = rec['ANO']
    MES = rec['MES']
    UF = rec['UF']
    MUNICIPIO = rec['MUNICIPIO']
    PAIS = rec['PAIS']
    CONTINENTE = rec['CONTINENTE']
    SEXO = rec['SEXO']
    TIPO_VISTO = rec['TIPO_VISTO']
    TIPOLOGIA_EXTRATOR = rec['TIPOLOGIA_EXTRATOR']
    TIPO_MOVIMENTO = rec['TIPO_MOVIMENTO']
    ADMITIDOS_DESLIGADOS = rec['ADMITIDOS_DESLIGADOS']
    eixoX = rec['eixoX']
    series = rec['series']

    query = vd(keep)

    pathName = '/'.join((dataFile.root_path, 'csv'))

    content = query.downloadContent(ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, SEXO, TIPO_VISTO, TIPOLOGIA_EXTRATOR, TIPO_MOVIMENTO, ADMITIDOS_DESLIGADOS, table,
        eixoX, series, pathName)

    return content
