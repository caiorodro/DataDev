
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

dataUser = Blueprint('dataUser', __name__)

@dataUser.route('/validaLogin', methods=['POST'])
def validaLogin():
    jsonData = json.loads(request.get_data())

    user1 =  jsonData['EMAIL']
    password = jsonData['SENHA']

    user = Usuario()
    backData = user.validaLogin(user1, password)

    del user

    return backData

@dataUser.route('/recoverPass', methods=['POST'])
def recoverPass():
    jsonData = json.loads(request.get_data())

    user1 =  jsonData['EMAIL']

    user = Usuario()
    user.recoverPass(user1)

    del user

    return "Ok"

@dataUser.route('/carregaUsuarios', methods=['POST'])
def carregaUsuarios():
    rec = json.loads(request.get_data())

    user = Usuario(rec['keep'])
    result = user.carregaUsuarios()

    del user

    return result

@dataUser.route('/buscaUsuario', methods=['POST'])
def buscaUsuario():

    rec = json.loads(request.get_data())

    ID_USUARIO = rec['ID_USUARIO']
    keep = rec['keep']

    user = Usuario(keep)
    result = user.buscaUsuario(ID_USUARIO)

    del user

    return result

@dataUser.route('/salvaUsuario', methods=['POST'])
def salvaUsuario():
    rec = json.loads(request.get_data())

    ID_USUARIO = rec['ID_USUARIO']
    NOME_USUARIO = rec['NOME_USUARIO']
    EMAIL_USUARIO = rec['EMAIL_USUARIO']
    SENHA_USUARIO = rec['SENHA_USUARIO']
    TIPO_USUARIO = rec['TIPO_USUARIO']
    USUARIO_ATIVO = rec['USUARIO_ATIVO']
    keep = rec['keep']

    user = Usuario(keep)
    user.salvaUsuario(ID_USUARIO, NOME_USUARIO, SENHA_USUARIO, EMAIL_USUARIO, TIPO_USUARIO, USUARIO_ATIVO)

    del user

    return "Ok"

@dataUser.route('/deletaUsuario', methods=['POST'])
def deletaUsuario():
    rec = json.loads(request.get_data())

    ID_USUARIO = rec['ID_USUARIO']
    keep = rec['keep']

    user = Usuario(keep)
    user.deletaUsuario(ID_USUARIO)

    del user

    return "Ok"
