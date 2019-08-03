import os
from flask import Blueprint
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import redirect
from flask import url_for
import json
from app.Queries import viewData as vd

cwd = os.getcwd()

dataQuery = Blueprint('dataQuery', __name__)

@dataQuery.route('/viewGrid', methods=['POST'])
def viewGrid():
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

    vd1 = vd(keep)

    result = vd1.viewGrid(ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, SEXO, TIPO_VISTO, TIPOLOGIA_EXTRATOR, TIPO_MOVIMENTO, ADMITIDOS_DESLIGADOS, table,
        eixoX, series)

    del vd1

    return result

@dataQuery.route('/viewChart', methods=['POST'])
def viewChart():
    rec = json.loads(request.get_data())

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
    table = rec['table']

    vd1 = vd(keep)

    result = vd1.viewChart(ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, SEXO, TIPO_VISTO, TIPOLOGIA_EXTRATOR, TIPO_MOVIMENTO, ADMITIDOS_DESLIGADOS,
        table, eixoX, series)

    del vd1

    return result
