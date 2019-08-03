import json
from flask import jsonify
import app.base.QException as qex
import app.base.QModel as ctx
from app.base.hBase import hBase
from venv.config import Config as config

class FiltrosCTPS(hBase):

    def __init__(self, keep=None):
        super().__init__(keep)

    def carregaFiltroAnosMeses(self):

        select1 = ctx.session.query(
            ctx.mapCTPS.ANO,
            ctx.mapCTPS.MES).distinct().all()

        lista = []

        [(lista.append((
            row.ANO,
            row.MES
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroPais(self):
    
        select1 = ctx.session.query(
            ctx.mapCTPS.PAIS).distinct().order_by(ctx.mapCTPS.PAIS).all()

        lista = []

        [(lista.append((
            row.PAIS
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroContinente(self):

        select1 = ctx.session.query(
            ctx.mapCTPS.CONTINENTE).distinct().order_by(ctx.mapCTPS.CONTINENTE).all()

        lista = []

        [(lista.append((
            row.CONTINENTE
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroSexo(self):

        select1 = ctx.session.query(
            ctx.mapCTPS.SEXO).distinct().all()

        lista = []

        [(lista.append((
            row.SEXO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroUF(self):
        
        select1 = ctx.session.query(
            ctx.mapCTPS.UF).distinct().order_by(ctx.mapCTPS.UF).all()

        lista = []

        [(lista.append((
            row.UF
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroMunicipio(self, UF):
    
        select1 = ctx.session.query(
            ctx.mapCTPS.MUNICIPIO).distinct().filter(ctx.mapCTPS.UF == UF).order_by(ctx.mapCTPS.MUNICIPIO).all()

        lista = []

        [(lista.append((
            row.MUNICIPIO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def __close(self):
        try:
            ctx.session.close()
            ctx.conn.close()
        except:
            pass
    
    def __del__(self):
        self.__close()

class FiltrosCGIL(hBase):
    
    def __init__(self, keep=None):
        super().__init__(keep)

    def carregaFiltroAnosMeses(self):

        select1 = ctx.session.query(
            ctx.mapCGIL.ANO,
            ctx.mapCGIL.MES).distinct().all()

        lista = []

        [(lista.append((
            row.ANO,
            row.MES
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroPais(self):
    
        select1 = ctx.session.query(
            ctx.mapCGIL.PAIS).distinct().order_by(ctx.mapCGIL.PAIS).all()

        lista = []

        [(lista.append((
            row.PAIS
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroContinente(self):

        select1 = ctx.session.query(
            ctx.mapCGIL.CONTINENTE).distinct().order_by(ctx.mapCGIL.CONTINENTE).all()

        lista = []

        [(lista.append((
            row.CONTINENTE
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroSexo(self):

        select1 = ctx.session.query(
            ctx.mapCGIL.SEXO).distinct().all()

        lista = []

        [(lista.append((
            row.SEXO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroUF(self):
        
        select1 = ctx.session.query(
            ctx.mapCGIL.UF).distinct().order_by(ctx.mapCGIL.UF).all()

        lista = []

        [(lista.append((
            row.UF
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroMunicipio(self, UF):
    
        select1 = ctx.session.query(
            ctx.mapCGIL.MUNICIPIO).distinct().where(ctx.mapCGIL.UF == UF).order_by(ctx.mapCGIL.MUNICIPIO).all()

        lista = []

        [(lista.append((
            row.MUNICIPIO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroTipoVisto(self):
        select1 = ctx.session.query(
            ctx.mapCGIL.TIPO_VISTO).distinct().all()

        lista = []

        [(lista.append((
            row.TIPO_VISTO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def __close(self):
        try:
            ctx.session.close()
            ctx.conn.close()
        except:
            pass
    
    def __del__(self):
        self.__close()

class FiltrosCAGED(hBase):
    
    def __init__(self, keep=None):
        super().__init__(keep)

    def carregaFiltroAnosMeses(self):

        select1 = ctx.session.query(
            ctx.mapCAGED.ANO,
            ctx.mapCAGED.MES).distinct().all()

        lista = []

        [(lista.append((
            row.ANO,
            row.MES
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroPais(self):
    
        select1 = ctx.session.query(
            ctx.mapCAGED.PAIS).distinct().order_by(ctx.mapCAGED.PAIS).all()

        lista = []

        [(lista.append((
            row.PAIS
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroContinente(self):

        select1 = ctx.session.query(
            ctx.mapCAGED.CONTINENTE).distinct().order_by(ctx.mapCAGED.CONTINENTE).all()

        lista = []

        [(lista.append((
            row.CONTINENTE
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroSexo(self):

        select1 = ctx.session.query(
            ctx.mapCAGED.SEXO).distinct().all()

        lista = []

        [(lista.append((
            row.SEXO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroUF(self):
        
        select1 = ctx.session.query(
            ctx.mapCAGED.UF).distinct().order_by(ctx.mapCAGED.UF).all()

        lista = []

        [(lista.append((
            row.UF
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroMunicipio(self, UF):
    
        select1 = ctx.session.query(
            ctx.mapCAGED.MUNICIPIO).distinct().filter(ctx.mapCAGED.UF == UF).order_by(ctx.mapCAGED.MUNICIPIO).all()

        lista = []

        [(lista.append((
            row.MUNICIPIO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroAdmitidosDesligados(self):
        select1 = ctx.session.query(
            ctx.mapCAGED.ADMITIDOS_DESLIGADOS).distinct().all()

        lista = []

        [(lista.append((
            row.ADMITIDOS_DESLIGADOS
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def __close(self):
        try:
            ctx.session.close()
            ctx.conn.close()
        except:
            pass
    
    def __del__(self):
        self.__close()

class FiltrosRAIS(hBase):

    def __init__(self, keep=None):
        super().__init__(keep)

    def carregaFiltroAnosMeses(self):

        select1 = ctx.session.query(
            ctx.mapRAIS.ANO).distinct().all()

        lista = []

        [(lista.append((
            row.ANO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroPais(self):
    
        select1 = ctx.session.query(
            ctx.mapRAIS.PAIS).distinct().order_by(ctx.mapRAIS.PAIS).all()

        lista = []

        [(lista.append((
            row.PAIS
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroContinente(self):

        select1 = ctx.session.query(
            ctx.mapRAIS.CONTINENTE).distinct().order_by(ctx.mapRAIS.CONTINENTE).all()

        lista = []

        [(lista.append((
            row.CONTINENTE
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroSexo(self):

        select1 = ctx.session.query(
            ctx.mapRAIS.SEXO).distinct().all()

        lista = []

        [(lista.append((
            row.SEXO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroUF(self):
        
        select1 = ctx.session.query(
            ctx.mapRAIS.UF).distinct().order_by(ctx.mapRAIS.UF).all()

        lista = []

        [(lista.append((
            row.UF
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroMunicipio(self, UF):
    
        select1 = ctx.session.query(
            ctx.mapRAIS.MUNICIPIO).distinct().where(ctx.mapRAIS.UF == UF).order_by(ctx.mapRAIS.MUNICIPIO).all()

        lista = []

        [(lista.append((
            row.MUNICIPIO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def __close(self):
        try:
            ctx.session.close()
            ctx.conn.close()
        except:
            pass
    
    def __del__(self):
        self.__close()

class FiltrosSISMIGRA_ENTRADA(hBase):
    
    def __init__(self, keep=None):
        super().__init__(keep)

    def carregaFiltroAnosMeses(self):

        select1 = ctx.session.query(
            ctx.mapSISMIGRA_ENTRADA.ANO,
            ctx.mapSISMIGRA_ENTRADA.MES).distinct().all()

        lista = []

        [(lista.append((
            row.ANO,
            row.MES
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroPais(self):
    
        select1 = ctx.session.query(
            ctx.mapSISMIGRA_ENTRADA.PAIS).distinct().order_by(ctx.mapSISMIGRA_ENTRADA.PAIS).all()

        lista = []

        [(lista.append((
            row.PAIS
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroContinente(self):

        select1 = ctx.session.query(
            ctx.mapSISMIGRA_ENTRADA.CONTINENTE).distinct().order_by(ctx.mapSISMIGRA_ENTRADA.CONTINENTE).all()

        lista = []

        [(lista.append((
            row.CONTINENTE
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroSexo(self):

        select1 = ctx.session.query(
            ctx.mapSISMIGRA_ENTRADA.SEXO).distinct().all()

        lista = []

        [(lista.append((
            row.SEXO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroUF(self):
        
        select1 = ctx.session.query(
            ctx.mapSISMIGRA_ENTRADA.UF).distinct().order_by(ctx.mapSISMIGRA_ENTRADA.UF).all()

        lista = []

        [(lista.append((
            row.UF
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroMunicipio(self, UF):
    
        select1 = ctx.session.query(
            ctx.mapSISMIGRA_ENTRADA.MUNICIPIO).distinct().where(ctx.mapSISMIGRA_ENTRADA.UF == UF).order_by(ctx.mapSISMIGRA_ENTRADA.MUNICIPIO).all()

        lista = []

        [(lista.append((
            row.MUNICIPIO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroTIPOLOGIA_EXTRATOR(self):
        select1 = ctx.session.query(
            ctx.mapSISMIGRA_ENTRADA.TIPOLOGIA_ENTRADA).distinct().all()

        lista = []

        [(lista.append((
            row.TIPOLOGIA_ENTRADA
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def __close(self):
        try:
            ctx.session.close()
            ctx.conn.close()
        except:
            pass
    
    def __del__(self):
        self.__close()

class FiltrosSISMIGRA_REGISTRO(hBase):
    
    def __init__(self, keep=None):
        super().__init__(keep)

    def carregaFiltroAnosMeses(self):

        select1 = ctx.session.query(
            ctx.mapSISMIGRA_REGISTRO.ANO,
            ctx.mapSISMIGRA_REGISTRO.MES).distinct().all()

        lista = []

        [(lista.append((
            row.ANO,
            row.MES
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroPais(self):
    
        select1 = ctx.session.query(
            ctx.mapSISMIGRA_REGISTRO.PAIS).distinct().order_by(ctx.mapSISMIGRA_REGISTRO.PAIS).all()

        lista = []

        [(lista.append((
            row.PAIS
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroContinente(self):

        select1 = ctx.session.query(
            ctx.mapSISMIGRA_REGISTRO.CONTINENTE).distinct().order_by(ctx.mapSISMIGRA_REGISTRO.CONTINENTE).all()

        lista = []

        [(lista.append((
            row.CONTINENTE
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroSexo(self):

        select1 = ctx.session.query(
            ctx.mapSISMIGRA_REGISTRO.SEXO).distinct().all()

        lista = []

        [(lista.append((
            row.SEXO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroUF(self):
    
        select1 = ctx.session.query(
            ctx.mapSISMIGRA_REGISTRO.UF).distinct().order_by(ctx.mapSISMIGRA_REGISTRO.UF).all()

        lista = []

        [(lista.append((
            row.UF
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroMunicipio(self, UF):
    
        select1 = ctx.session.query(
            ctx.mapSISMIGRA_REGISTRO.MUNICIPIO).distinct().where(ctx.mapSISMIGRA_REGISTRO.UF == UF).order_by(ctx.mapSISMIGRA_REGISTRO.MUNICIPIO).all()

        lista = []

        [(lista.append((
            row.MUNICIPIO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroTIPOLOGIA_EXTRATOR(self):
        select1 = ctx.session.query(
            ctx.mapSISMIGRA_REGISTRO.TIPOLOGIA_ENTRADA).distinct().all()

        lista = []

        [(lista.append((
            row.TIPOLOGIA_ENTRADA
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def __close(self):
        try:
            ctx.session.close()
            ctx.conn.close()
        except:
            pass
    
    def __del__(self):
        self.__close()

class FiltrosSTI(hBase):
    
    def __init__(self, keep=None):
        super().__init__(keep)

    def carregaFiltroAnosMeses(self):

        select1 = ctx.session.query(
            ctx.mapSTI.ANO,
            ctx.mapSTI.MES).distinct().all()

        lista = []

        [(lista.append((
            row.ANO,
            row.MES
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroPais(self):
    
        select1 = ctx.session.query(
            ctx.mapSTI.PAIS).distinct().order_by(ctx.mapSTI.PAIS).all()

        lista = []

        [(lista.append((
            row.PAIS
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroContinente(self):

        select1 = ctx.session.query(
            ctx.mapSTI.CONTINENTE).distinct().order_by(ctx.mapSTI.CONTINENTE).all()

        lista = []

        [(lista.append((
            row.CONTINENTE
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroSexo(self):

        select1 = ctx.session.query(
            ctx.mapSTI.SEXO).distinct().all()

        lista = []

        [(lista.append((
            row.SEXO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroUF(self):

        select1 = ctx.session.query(
            ctx.mapSTI.UF).distinct().order_by(ctx.mapSTI.UF).all()

        lista = []

        [(lista.append((
            row.UF
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroMunicipio(self, UF):
    
        select1 = ctx.session.query(
            ctx.mapSTI.MUNICIPIO).distinct().where(ctx.mapSTI.UF == UF).order_by(ctx.mapSTI.MUNICIPIO).all()

        lista = []

        [(lista.append((
            row.MUNICIPIO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroTIPO_MOVIMENTO(self):
        select1 = ctx.session.query(
            ctx.mapSTI.TIPO_MOVIMENTO).distinct().all()

        lista = []

        [(lista.append((
            row.TIPO_MOVIMENTO
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def carregaFiltroTIPOLOGIA_EXTRATOR(self):
        select1 = ctx.session.query(
            ctx.mapSTI.TIPOLOGIA_ENTRADA).distinct().all()

        lista = []

        [(lista.append((
            row.TIPOLOGIA_ENTRADA
            ))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def __close(self):
        try:
            ctx.session.close()
            ctx.conn.close()
        except:
            pass
    
    def __del__(self):
        self.__close()
