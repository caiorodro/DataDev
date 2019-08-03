import json
from flask import jsonify
import app.base.QException as qex
import app.base.QModel as ctx 
from app.base.hBase import hBase
from app.base.qMail import qMail

class Usuario(hBase):

    def __init__(self, keep=None):
        super().__init__(keep)

    def carregaUsuarios(self):
        btnEdit = '<button class="btn btn-primary waves-effect waves-light btn-sm m-b-5" onclick="edita({});" title="Editar"><i class="ti-pencil"></i></button>'
        btnDelete = '<button class="btn btn-danger waves-effect waves-light btn-sm m-b-5" onclick="deleta({});" title="Deletar"><i class="ti-trash"></i></button>'

        select1 = ctx.session.query(
            ctx.mapUsuario.ID_USUARIO,
            ctx.mapUsuario.NOME_USUARIO,
            ctx.mapUsuario.EMAIL_USUARIO,
            ctx.mapUsuario.USUARIO_ATIVO,
            ctx.mapUsuario.TIPO_USUARIO).order_by(ctx.mapUsuario.NOME_USUARIO).all()

        lista = []

        [(lista.append((row.ID_USUARIO,
            row.NOME_USUARIO,
            row.EMAIL_USUARIO,
            'Sim' if row.USUARIO_ATIVO else 'Não',
            'Administrador' if row.TIPO_USUARIO else 'Usuário',
            btnEdit.format(str(row.ID_USUARIO)), 
            btnDelete.format(str(row.ID_USUARIO))))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def salvaUsuario(self, ID_USUARIO, NOME_USUARIO, SENHA_USUARIO, EMAIL_USUARIO, TIPO_USUARIO, USUARIO_ATIVO):

        pass1 = SENHA_USUARIO

        cmd = None

        if ID_USUARIO > 0:

            cmd = ctx.usuario.update().values(
                NOME_USUARIO = NOME_USUARIO.upper(),
                SENHA_USUARIO = pass1,
                EMAIL_USUARIO = EMAIL_USUARIO.lower(),
                TIPO_USUARIO = TIPO_USUARIO,
                USUARIO_ATIVO = USUARIO_ATIVO).\
                    where(ctx.mapUsuario.ID_USUARIO == ID_USUARIO)

        if ID_USUARIO == 0:
            cmd = ctx.usuario.insert().values(
                NOME_USUARIO = NOME_USUARIO.upper(),
                SENHA_USUARIO = pass1,
                EMAIL_USUARIO = EMAIL_USUARIO.lower(),
                TIPO_USUARIO = TIPO_USUARIO,
                USUARIO_ATIVO = USUARIO_ATIVO)

        ctx.session.execute(cmd)
        ctx.session.commit()

    def deletaUsuario(self, ID_USUARIO):
        del1 = ctx.usuario.delete()\
            .where(ctx.mapUsuario.ID_USUARIO == ID_USUARIO)

        ctx.session.execute(del1)
        ctx.session.commit()

    def buscaUsuario(self, ID_USUARIO):
        select1 = ctx.session.query(
            ctx.mapUsuario.ID_USUARIO,
            ctx.mapUsuario.NOME_USUARIO,
            ctx.mapUsuario.SENHA_USUARIO,
            ctx.mapUsuario.EMAIL_USUARIO,
            ctx.mapUsuario.USUARIO_ATIVO,
            ctx.mapUsuario.TIPO_USUARIO).filter(ctx.mapUsuario.ID_USUARIO == ID_USUARIO).all()

        lista = super().toDict(select1)

        try:
            for item in lista:
                item['USUARIO_ATIVO'] = float(item['USUARIO_ATIVO'])
        except:
            pass

        return str(lista)

    def validaLogin(self, EMAIL_USUARIO, SENHA_USUARIO):
        try:
            rec = ctx.session.query(ctx.mapUsuario).\
                filter(ctx.mapUsuario.EMAIL_USUARIO == EMAIL_USUARIO).first()
        except:
            return qex.throw('Usuário não cadastrado')

        if rec == None:
            return qex.throw('Usuário não cadastrado')

        # senhaDecifrada = Cifra.decifra(rec.SENHA_USUARIO)

        if rec.SENHA_USUARIO != SENHA_USUARIO:
            return qex.throw('Senha incorreta')

        if float(rec.TIPO_USUARIO) != 1:
            return qex.throw('Acesso negado')

        # keep = Cifra.cifra(super().TrataDataHora()).decode('utf8')
        keep = '8Kd4KmTesIXTOI8awHuhod1X7ERl3divuinW5b8CSNhcO2kITIwUkJDzZpHgZyXx'

        return json.dumps({ 'status': 'OK', 'id': rec.ID_USUARIO, 'TIPO': rec.TIPO_USUARIO, 'keep': keep })

    def recoverPass(self, EMAIL_USUARIO):
        rec = ctx.session.query(ctx.mapUsuario).\
        filter(ctx.mapUsuario.EMAIL_USUARIO == EMAIL_USUARIO).first()

        if rec is None:
            return qex.throw('Usuário não cadastrado')

        mail = qMail('smtp.doran.com.br', 587, 'contato@doran.com.br', '56Runna01')
        mail.enviaInstrucoesNovaSenha(EMAIL_USUARIO, rec.ID_USUARIO)
        del mail

    def close(self):
        try:
            ctx.conn.close()
        except:
            pass

    def __del__(self):
        self.close()

# def listaUsuarios(NOME):
#     lista = select([ctx.usuario])

#     result = ctx.conn.execute(lista).fetchmany(5)

#     for item in result:
#         print(item.NOME_USUARIO)

# def transaction():
#     #sample
#     tran = ctx.conn.begin()

#     try:
#         update = ctx.usuario.update().values(
#             NOME_USUARIO = 'CAIO DORAN',
#             SENHA_USUARIO = 'Ok').\
#                 where(ctx.usuario.c.ID_USUARIO == 1)

#         ctx.conn.execute(update)
#         tran.commit()
#     except:
#         tran.rollback()
#         raise

# def transactionWithSession():

#     try:
#         rec = ctx.session.query(ctx.mapUsuario).filter(ctx.mapUsuario.ID_USUARIO == 1).first()

#         rec.NOME_USUARIO = 'CAIO DORAN'

#         ctx.session.commit()
#     except:
#         ctx.session.rollback()
#         raise
#     finally:
#         ctx.session.close()
