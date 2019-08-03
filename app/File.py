import io
import os
import json, csv
import zipfile
from flask import jsonify
from sqlalchemy import func, desc
import app.base.QException as qex
import app.base.QModel as ctx
from app.base.hBase import hBase
from datetime import datetime
from app.base.mapTable import mapCTPS, mapCAGED, mapCGIL, mapRAIS, mapSISMIGRA_ENTRADA, mapSISMIGRA_REGISTRO, mapSTI, mapTEMP

class File(hBase):

    def __init__(self, keep=None):
        super().__init__(keep)

        self.__rowsBulkInsert = 15000
        self.__rowsInserted = 0

    def carregaFiles(self):
        btnDelete = '<button class="btn btn-danger waves-effect waves-light btn-sm m-b-5" onclick="deletaFile({});" title="Deletar"><i class="dripicons-trash"></i></button>'
        btnDownload = '<button class="btn btn-purple waves-effect waves-light btn-sm m-b-5" onclick="downloadContent({});" title="Visualizar"><i class="mdi mdi-view-headline"></i></button>'

        select1 = ctx.session.query(
            ctx.mapFile.ID_FILE,
            ctx.mapFile.FILE_NAME,
            ctx.mapFile.CONTENT_FILE,
            ctx.mapFile.DATE_FILE).order_by(desc(ctx.mapFile.DATE_FILE)).limit(100)

        lista = []

        [(lista.append((btnDelete.format(str(row.ID_FILE)),
            row.ID_FILE,
            row.FILE_NAME,
            row.DATE_FILE.strftime('%d-%m-%Y %H:%M'),
            ''.join((str(round(len(row.CONTENT_FILE) / self.__rowsBulkInsert, 2)), ' MB')),
            btnDownload.format(str(row.ID_FILE))))) for row in select1]

        retorno = super().toJson(lista)

        return retorno

    def gravaArquivoNaBase(self, fileName, content):

        csvPath = '/'.join((os.getcwd(), 'csv'))
        finalFile = ''.join((csvPath, '/', fileName[0: fileName.find('.')], '.csv'))

        try:
            with zipfile.ZipFile(io.BytesIO(content)) as zip_ref:
                zip_ref.extractall(csvPath)
        except:
            csvPath = '/tmp'
            finalFile = ''.join((csvPath, '/', fileName[0: fileName.find('.')], '.csv'))

            with zipfile.ZipFile(io.BytesIO(content)) as zip_ref:
                zip_ref.extractall(csvPath)

        msec = datetime.now().microsecond
        xfile = fileName.lower()
        names = ['ctps', 'caged', 'cgil', 'rais', 'sismigra_entrada', 'sismigra_registro', 'sti']
        
        _table = list(filter(lambda name: xfile.startswith(name), names))[0]

        anos = self.__gravaTabelaTemporaria(msec, _table, finalFile)

        if _table == 'ctps':
            [(ctx.session.query(ctx.mapCTPS).filter(ctx.mapCTPS.ANO == ano).delete(),
              ctx.session.commit()) 
              for ano in anos]

            retorno = self.__gravaCTPS(finalFile)

        elif _table == 'caged':
            [(ctx.session.query(ctx.mapCAGED).filter(ctx.mapCAGED.ANO == ano).delete(),
              ctx.session.commit()) 
              for ano in anos]

            retorno = self.__gravaCAGED(finalFile)

        elif _table == 'cgil':
            [(ctx.session.query(ctx.mapCGIL).filter(ctx.mapCGIL.ANO == ano).delete(),
              ctx.session.commit()) 
              for ano in anos]

            retorno = self.__gravaCGIL(finalFile)

        elif _table == 'rais':
            [(ctx.session.query(ctx.mapRAIS).filter(ctx.mapRAIS.ANO == ano).delete(),
              ctx.session.commit()) 
              for ano in anos]

            retorno = self.__gravaRAIS(finalFile)

        elif _table == 'sismigra_entrada':
            [(ctx.session.query(ctx.mapSISMIGRA_ENTRADA).filter(ctx.mapSISMIGRA_ENTRADA.ANO == ano).delete(),
              ctx.session.commit()) 
              for ano in anos]

            retorno = self.__gravaSISMIGRA_ENTRADA(finalFile)

        elif _table == 'sismigra_registro':
            [(ctx.session.query(ctx.mapSISMIGRA_REGISTRO).filter(ctx.mapSISMIGRA_REGISTRO.ANO == ano).delete(),
              ctx.session.commit()) 
              for ano in anos]

            retorno = self.__gravaSISMIGRA_REGISTRO(finalFile)

        elif _table == 'sti':
            [(ctx.session.query(ctx.mapSTI).filter(ctx.mapSTI.ANO == ano).delete(),
              ctx.session.commit()) for ano in anos]

            retorno = self.__gravaSTI(finalFile)

        strOk = json.dumps({ 'status': 'OK', 'rowsInserted': finalFile[finalFile.rindex('/') + 1:] + ': ' + str(self.__rowsInserted) })  

        return strOk if retorno is None else retorno

    def __gravaCTPS(self, finalFile):
        
        recs = []

        firstLine = True

        try:
            with open(finalFile, mode='rb') as file:

                for lineIn in file:
                    
                    if firstLine:
                        firstLine = False
                        continue

                    row = lineIn.decode('utf-8').replace('"', '').replace('\r\n', '').split(';')

                    recs.append({
                        'ID_CTPS': 0,
                        'ANO': row[0],
                        'MES': row[1],
                        'UF': row[2],
                        'MUNICIPIO': row[3],
                        'PAIS': row[4],
                        'CONTINENTE': row[5],
                        'SEXO': row[6]
                        })

                    if (len(recs) % self.__rowsBulkInsert) == 0:
                        self.__bulkInsert(mapCTPS, recs, 1)
                        recs = []

            if len(recs) > 0:
                self.__bulkInsert(mapCTPS, recs, 1)

        except ValueError as err:
            return qex.throw(err)

    def __gravaCAGED(self, finalFile):
        
        recs = []

        firstLine = True

        try:
            with open(finalFile, mode='rb') as file:

                for lineIn in file:
                    
                    if firstLine:
                        firstLine = False
                        continue

                    row = lineIn.decode('utf-8').replace('"', '').replace('\r\n', '').split(';')

                    recs.append({
                        'ID_CAGED': 0,
                        'ANO': row[0],
                        'MES': row[1],
                        'UF': row[2],
                        'MUNICIPIO': row[3],
                        'PAIS': row[4],
                        'CONTINENTE': row[5],
                        'ADMITIDOS_DESLIGADOS': row[6],
                        'SEXO': row[7]
                        })

                    if (len(recs) % self.__rowsBulkInsert) == 0:
                        self.__bulkInsert(mapCAGED, recs, 1)
                        recs = []

            if len(recs) > 0:
                self.__bulkInsert(mapCAGED, recs, 1)

        except ValueError as err:
            return qex.throw(err.args[0])

    def __gravaCGIL(self, finalFile):
        
        recs = []

        firstLine = True

        try:
            with open(finalFile, mode='rb') as file:

                for lineIn in file:
                    
                    if firstLine:
                        firstLine = False
                        continue

                    row = lineIn.decode('utf-8').replace('"', '').replace('\r\n', '').split(';')

                    recs.append({
                        'ID_CGIL': 0,
                        'ANO': row[0],
                        'MES': row[1],
                        'UF': row[2],
                        'PAIS': row[3],
                        'CONTINENTE': row[4],
                        'TIPO_VISTO': row[5],
                        'SEXO': row[6]
                        })

                    if (len(recs) % self.__rowsBulkInsert) == 0:
                        self.__bulkInsert(mapCGIL, recs, 1)
                        recs = []

            if len(recs) > 0:
                self.__bulkInsert(mapCGIL, recs, 1)

        except ValueError as err:
            return qex.throw(err)

    def __gravaRAIS(self, finalFile):
        
        recs = []

        firstLine = True

        try:
            with open(finalFile, mode='rb') as file:

                for lineIn in file:
                    
                    if firstLine:
                        firstLine = False
                        continue

                    row = lineIn.decode('utf-8').replace('"', '').replace('\r\n', '').split(';')

                    recs.append({
                        'ID_RAIS': 0,
                        'ANO': row[0],
                        'UF': row[1],
                        'MUNICIPIO': row[2],
                        'PAIS': row[3],
                        'CONTINENTE': row[4],
                        'SEXO': row[5]
                        })

                    if (len(recs) % self.__rowsBulkInsert) == 0:
                        self.__bulkInsert(mapRAIS, recs, 1)
                        recs = []

            if len(recs) > 0:
                self.__bulkInsert(mapRAIS, recs, 1)

        except ValueError as err:
            return qex.throw(err)

    def __gravaSISMIGRA_ENTRADA(self, finalFile):
        
        recs = []

        firstLine = True

        try:
            with open(finalFile, mode='rb') as file:

                for lineIn in file:
                    
                    if firstLine:
                        firstLine = False
                        continue

                    row = lineIn.decode('utf-8').replace('"', '').split(';')

                    recs.append({
                        'ID_MIGRA': 0,
                        'ANO': row[0],
                        'MES': row[1],
                        'UF': row[2],
                        'MUNICIPIO': row[3],
                        'PAIS': row[4],
                        'CONTINENTE': row[5],
                        'TIPOLOGIA_ENTRADA': row[6],
                        'SEXO': row[7]
                        })

                    if (len(recs) % self.__rowsBulkInsert) == 0:
                        self.__bulkInsert(mapSISMIGRA_ENTRADA, recs, 1)
                        recs = []

            if len(recs) > 0:
                self.__bulkInsert(mapSISMIGRA_ENTRADA, recs, 1)

        except ValueError as err:
            return qex.throw(err)

    def __gravaSISMIGRA_REGISTRO(self, finalFile):
        
        recs = []

        firstLine = True

        try:
            with open(finalFile, mode='rb') as file:

                for lineIn in file:
                    
                    if firstLine:
                        firstLine = False
                        continue

                    row = lineIn.decode('utf-8').replace('"', '').replace('\r\n', '').split(';')

                    recs.append({
                        'ID_MIGRA': 0,
                        'ANO': row[0],
                        'MES': row[1],
                        'UF': row[2],
                        'MUNICIPIO': row[3],
                        'PAIS': row[4],
                        'CONTINENTE': row[5],
                        'TIPOLOGIA_ENTRADA': row[6],
                        'SEXO': row[7]
                        })

                    if (len(recs) % self.__rowsBulkInsert) == 0:
                        self.__bulkInsert(mapSISMIGRA_REGISTRO, recs, 1)
                        recs = []

            if len(recs) > 0:
                self.__bulkInsert(mapSISMIGRA_REGISTRO, recs, 1)

        except ValueError as err:
            return qex.throw(err)

    def __gravaSTI(self, finalFile):
        
        recs = []

        firstLine = True

        try:
            with open(finalFile, mode='rb') as file:

                for lineIn in file:
                    
                    if firstLine:
                        firstLine = False
                        continue

                    row = lineIn.decode('utf-8').replace('"', '').replace('\r\n', '').split(';')

                    recs.append({
                        'ID_STI': 0,
                        'ANO': row[0],
                        'MES': row[1],
                        'UF': row[2],
                        'PAIS': row[3],
                        'CONTINENTE': row[4],
                        'TIPO_MOVIMENTO': row[5],
                        'TIPOLOGIA_ENTRADA': row[6],
                        'SEXO': row[7]
                        })

                    if (len(recs) % self.__rowsBulkInsert) == 0:
                        self.__bulkInsert(mapSTI, recs, 1)
                        recs = []

                file.close()

            if len(recs) > 0:
                self.__bulkInsert(mapSTI, recs, 1)

        except ValueError as err:
            return qex.throw(err)

    def __gravaTabelaTemporaria(self, msec, _table, finalFile):
 
        recs = []

        firstLine = True

        try:
            with open(finalFile, mode='rb') as file:

                for lineIn in file:

                    if firstLine:
                        firstLine = False
                        continue

                    row = lineIn.decode('utf-8').replace('"', '').replace('\r\n', '').split(';')

                    recs.append({
                        'ID_TEMP': 0,
                        'MILISEC': msec,
                        'TABELA_ORIGEM': _table,
                        'ANO': row[0]
                        })

                    if (len(recs) % self.__rowsBulkInsert) == 0:
                        self.__bulkInsert(mapTEMP, recs)
                        recs = []

            if len(recs) > 0:
                self.__bulkInsert(mapTEMP, recs)

        except ValueError as err:
            return qex.throw(err)

        select1 = ctx.session.query(
            ctx.mapTEMP.ANO).distinct().filter(ctx.mapTEMP.MILISEC == msec and ctx.mapTEMP.TABELA_ORIGEM == _table).all()

        lista = []

        [(lista.append((
            row.ANO
            ))) for row in select1]
        
        return lista

    def __bulkInsert(self, xTable, recs, toCount=None):
        if len(recs) > 0:
            try:
                ctx.session.bulk_insert_mappings(xTable, recs)
                ctx.session.commit()

                if toCount == 1:
                    self.__rowsInserted += len(recs)
            except:
                ctx.session.rollback()
                self.__close()

                raise ValueError('Problemas ao importar um ou mais registros entre as linhas [{}] e [{}]'
                        .format(str(self.__rowsInserted), str(self.__rowsInserted + self.__rowsBulkInsert)))

    def deletaFile(self, ID_FILE):
        try:
            cmd = ctx.file.delete()\
                .where(ctx.mapFile.ID_FILE == ID_FILE)

            ctx.session.execute(cmd)
            ctx.session.commit()
        except:
            ctx.session.rollback()

    def downloadContent(self, ID_FILE, PATH_NAME, ID_USUARIO):
        select1 = ctx.session.query(ctx.mapFile.CONTENT_FILE,
            ctx.mapFile.FILE_NAME,
            ctx.mapFile.DATE_FILE)\
            .filter(ctx.mapFile.ID_FILE == ID_FILE).all()

        content = ''
        name = ''
        datex = ''

        for item in select1:
            content = item.CONTENT_FILE.decode('utf-8')
            name = item.FILE_NAME
            datex = item.DATE_FILE.strftime('%d-%m-%Y %H:%M'),

        sp1 = name.split('.')
        fileName = ''.join((sp1[0], str(ID_USUARIO), '.', sp1[1]))

        PATH_NAME = '/'.join((PATH_NAME, fileName))

        self.__saveFile(content, PATH_NAME)

        maxLength = 3000

        if len(content) > maxLength:
            content = content[0: maxLength] + '...'

        return json.dumps({ 'status': 'OK', 'content': content, 'name': name, 'date': datex, 'link': fileName })

    def __saveFile(self, CONTENT, PATH_NAME):

        try: 
            csvFile = open(PATH_NAME, "w+")
            csvFile.write(CONTENT)
        finally:
            csvFile.close()

    def __close(self):
        try:
            ctx.session.close()
            ctx.conn.close()
        except:
            pass

    def __del__(self):
        self.__close()
