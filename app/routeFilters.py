import os
from flask import Blueprint
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import redirect
from flask import url_for
import json
from app.Filtros import FiltrosCTPS, FiltrosCGIL, FiltrosCAGED, FiltrosRAIS, FiltrosSISMIGRA_ENTRADA, FiltrosSISMIGRA_REGISTRO, FiltrosSTI
from app.Queries import viewData as vd

cwd = os.getcwd()

dataFilter = Blueprint('dataFilter', __name__)

@dataFilter.route('/carregaFiltroAnosMeses', methods=['POST'])
def carregaFiltroAnosMeses():
    rec = json.loads(request.get_data())

    keep = rec['keep']
    item = rec['item']

    if item == 'CTPS':
        filtro = FiltrosCTPS(keep)
    elif item == 'CGIL':
        filtro = FiltrosCGIL(keep)
    elif item == 'CAGED':
        filtro = FiltrosCAGED(keep)
    elif item == 'RAIS':
        filtro = FiltrosRAIS(keep)
    elif item == 'SISMIGRA_ENTRADA':
        filtro = FiltrosSISMIGRA_ENTRADA(keep)
    elif item == 'SISMIGRA_REGISTRO':
        filtro = FiltrosSISMIGRA_REGISTRO(keep)
    elif item == 'STI':
        filtro = FiltrosSTI(keep)

    result = filtro.carregaFiltroAnosMeses()
    del filtro

    return result

@dataFilter.route('/carregaFiltroPais', methods=['POST'])
def carregaFiltroPais():
    rec = json.loads(request.get_data())

    keep = rec['keep']
    item = rec['item']

    if item == 'CTPS':
        filtro = FiltrosCTPS(keep)
    elif item == 'CGIL':
        filtro = FiltrosCGIL(keep)
    elif item == 'CAGED':
        filtro = FiltrosCAGED(keep)
    elif item == 'RAIS':
        filtro = FiltrosRAIS(keep)
    elif item == 'SISMIGRA_ENTRADA':
        filtro = FiltrosSISMIGRA_ENTRADA(keep)
    elif item == 'SISMIGRA_REGISTRO':
        filtro = FiltrosSISMIGRA_REGISTRO(keep)
    elif item == 'STI':
        filtro = FiltrosSTI(keep)

    result = filtro.carregaFiltroPais()
    del filtro

    return result

@dataFilter.route('/carregaFiltroContinente', methods=['POST'])
def carregaFiltroContinente():
    rec = json.loads(request.get_data())

    keep = rec['keep']
    item = rec['item']

    if item == 'CTPS':
        filtro = FiltrosCTPS(keep)
    elif item == 'CGIL':
        filtro = FiltrosCGIL(keep)
    elif item == 'CAGED':
        filtro = FiltrosCAGED(keep)
    elif item == 'RAIS':
        filtro = FiltrosRAIS(keep)
    elif item == 'SISMIGRA_ENTRADA':
        filtro = FiltrosSISMIGRA_ENTRADA(keep)
    elif item == 'SISMIGRA_REGISTRO':
        filtro = FiltrosSISMIGRA_REGISTRO(keep)
    elif item == 'STI':
        filtro = FiltrosSTI(keep)

    result = filtro.carregaFiltroContinente()
    del filtro

    return result

@dataFilter.route('/carregaFiltroSexo', methods=['POST'])
def carregaFiltroSexo():
    rec = json.loads(request.get_data())

    keep = rec['keep']
    item = rec['item']

    if item == 'CTPS':
        filtro = FiltrosCTPS(keep)
    elif item == 'CGIL':
        filtro = FiltrosCGIL(keep)
    elif item == 'CAGED':
        filtro = FiltrosCAGED(keep)
    elif item == 'RAIS':
        filtro = FiltrosRAIS(keep)
    elif item == 'SISMIGRA_ENTRADA':
        filtro = FiltrosSISMIGRA_ENTRADA(keep)
    elif item == 'SISMIGRA_REGISTRO':
        filtro = FiltrosSISMIGRA_REGISTRO(keep)
    elif item == 'STI':
        filtro = FiltrosSTI(keep)

    result = filtro.carregaFiltroSexo()
    del filtro

    return result

@dataFilter.route('/carregaFiltroUF', methods=['POST'])
def carregaFiltroUF():
    rec = json.loads(request.get_data())

    keep = rec['keep']
    item = rec['item']

    if item == 'CTPS':
        filtro = FiltrosCTPS(keep)
    elif item == 'CGIL':
        filtro = FiltrosCGIL(keep)
    elif item == 'CAGED':
        filtro = FiltrosCAGED(keep)
    elif item == 'RAIS':
        filtro = FiltrosRAIS(keep)
    elif item == 'SISMIGRA_ENTRADA':
        filtro = FiltrosSISMIGRA_ENTRADA(keep)
    elif item == 'SISMIGRA_REGISTRO':
        filtro = FiltrosSISMIGRA_REGISTRO(keep)
    elif item == 'STI':
        filtro = FiltrosSTI(keep)

    result = filtro.carregaFiltroUF()
    del filtro

    return result

@dataFilter.route('/carregaFiltroMunicipio', methods=['POST'])
def carregaFiltroMunicipio():
    rec = json.loads(request.get_data())

    keep = rec['keep']
    item = rec['item']
    UF = rec['UF']

    if item == 'CTPS':
        filtro = FiltrosCTPS(keep)
    elif item == 'CGIL':
        filtro = FiltrosCGIL(keep)
    elif item == 'CAGED':
        filtro = FiltrosCAGED(keep)
    elif item == 'RAIS':
        filtro = FiltrosRAIS(keep)
    elif item == 'SISMIGRA_ENTRADA':
        filtro = FiltrosSISMIGRA_ENTRADA(keep)
    elif item == 'SISMIGRA_REGISTRO':
        filtro = FiltrosSISMIGRA_REGISTRO(keep)
    elif item == 'STI':
        filtro = FiltrosSTI(keep)

    result = filtro.carregaFiltroMunicipio(UF)
    del filtro 

    return result

@dataFilter.route('/carregaFiltroTipologia_Extrator', methods=['POST'])
def carregaFiltroTipologia_Extrator():
    rec = json.loads(request.get_data())

    keep = rec['keep']
    item = rec['item']

    if item == 'CTPS':
        filtro = FiltrosCTPS(keep)
    elif item == 'CGIL':
        filtro = FiltrosCGIL(keep)
    elif item == 'CAGED':
        filtro = FiltrosCAGED(keep)
    elif item == 'RAIS':
        filtro = FiltrosRAIS(keep)
    elif item == 'SISMIGRA_ENTRADA':
        filtro = FiltrosSISMIGRA_ENTRADA(keep)
    elif item == 'SISMIGRA_REGISTRO':
        filtro = FiltrosSISMIGRA_REGISTRO(keep)
    elif item == 'STI':
        filtro = FiltrosSTI(keep)

    result = filtro.carregaFiltroTIPOLOGIA_EXTRATOR()
    del filtro

    return result

@dataFilter.route('/carregaFiltroTipoVisto', methods=['POST'])
def carregaFiltroTipoVisto():
    rec = json.loads(request.get_data())

    keep = rec['keep']
    item = rec['item']

    if item == 'CTPS':
        filtro = FiltrosCTPS(keep)
    elif item == 'CGIL':
        filtro = FiltrosCGIL(keep)
    elif item == 'CAGED':
        filtro = FiltrosCAGED(keep)
    elif item == 'RAIS':
        filtro = FiltrosRAIS(keep)
    elif item == 'SISMIGRA_ENTRADA':
        filtro = FiltrosSISMIGRA_ENTRADA(keep)
    elif item == 'SISMIGRA_REGISTRO':
        filtro = FiltrosSISMIGRA_REGISTRO(keep)
    elif item == 'STI':
        filtro = FiltrosSTI(keep)

    result = filtro.carregaFiltroTipoVisto()
    del filtro

    return result

@dataFilter.route('/carregaFiltroAdmitidosDesligados', methods=['POST'])
def carregaFiltroAdmitidosDesligados():
    rec = json.loads(request.get_data())

    keep = rec['keep']
    item = rec['item']

    if item == 'CTPS':
        filtro = FiltrosCTPS(keep)
    elif item == 'CGIL':
        filtro = FiltrosCGIL(keep)
    elif item == 'CAGED':
        filtro = FiltrosCAGED(keep)
    elif item == 'RAIS':
        filtro = FiltrosRAIS(keep)
    elif item == 'SISMIGRA_ENTRADA':
        filtro = FiltrosSISMIGRA_ENTRADA(keep)
    elif item == 'SISMIGRA_REGISTRO':
        filtro = FiltrosSISMIGRA_REGISTRO(keep)
    elif item == 'STI':
        filtro = FiltrosSTI(keep)

    result = filtro.carregaFiltroAdmitidosDesligados()
    del filtro

    return result

@dataFilter.route('/carregaFiltroTipoMovimento', methods=['POST'])
def carregaFiltroTipoMovimento():
    rec = json.loads(request.get_data())

    keep = rec['keep']
    item = rec['item']

    if item == 'CTPS':
        filtro = FiltrosCTPS(keep)
    elif item == 'CGIL':
        filtro = FiltrosCGIL(keep)
    elif item == 'CAGED':
        filtro = FiltrosCAGED(keep)
    elif item == 'RAIS':
        filtro = FiltrosRAIS(keep)
    elif item == 'SISMIGRA_ENTRADA':
        filtro = FiltrosSISMIGRA_ENTRADA(keep)
    elif item == 'SISMIGRA_REGISTRO':
        filtro = FiltrosSISMIGRA_REGISTRO(keep)
    elif item == 'STI':
        filtro = FiltrosSTI(keep)

    result = filtro.carregaFiltroTIPO_MOVIMENTO()
    del filtro

    return result

@dataFilter.route('/getTables', methods=['POST'])
def getTables():
    rec = json.loads(request.get_data())

    keep = rec['keep']    

    q = vd(keep)
    fields = q.getTables()

    del q

    return json.dumps({ 'status': 'OK', 'fields': fields })
