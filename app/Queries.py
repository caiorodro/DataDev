import json
from flask import jsonify
import app.base.QException as qex
import app.base.QModel as ctx
from app.base.hBase import hBase
import numpy as np
from sqlalchemy import text
from app.base.mapTable import mapCTPS, mapCGIL, mapCAGED, mapRAIS, mapSISMIGRA_ENTRADA, mapSISMIGRA_REGISTRO, mapSTI
from datetime import datetime
from werkzeug.exceptions import HTTPException

class viewData(hBase):

    def __init__(self, keep=None):
        """
        Classe de visualização de dados em chart (google) e datatable jquery

        params: 
            keep = chave para manter e identificar o acesso ao método

        """
        super().__init__(keep)

    def viewGrid(self, ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, SEXO, TIPO_VISTO, TIPOLOGIA_EXTRATOR, TIPO_MOVIMENTO, ADMITIDOS_DESLIGADOS, table,
                eixoX, series):
        """
        Visualização dos dados em formato datatable jQuery

        params: 
            ANO = array  (2019, 2018)
            MES = array ('JANEIRO', 'SETEMBRO')

        Returns: 
            array collection columns from selected table in query

        """

        table = table.lower()
        where = ''

        if len(ANO) > 0:
            where += ''.join(('| ANO IN(', ', '.join(map(str, ANO)), ')'))

        if len(MES) > 0:
            where += ''.join(('| MES IN(', ', '.join(map(lambda x: "'" + x + "'", MES)), ')'))

        if len(CONTINENTE) > 0:
            where += ''.join(('| CONTINENTE IN(', ', '.join(map(lambda x: "'" + x + "'", CONTINENTE)), ')'))

        if len(PAIS) > 0:
            where += ''.join(('| PAIS IN(', ', '.join(map(lambda x: "'" + x + "'", PAIS)), ')'))

        if len(UF) > 0:
            where += ''.join(('| UF IN(', ', '.join(map(lambda x: "'" + x + "'", UF)), ')'))

        if len(MUNICIPIO) > 0:
            where += ''.join(('| MUNICIPIO IN(', ', '.join(map(lambda x: "'" + x + "'", MUNICIPIO)), ')'))

        if len(SEXO) > 0:
            where += ''.join(('| SEXO IN(', ', '.join(map(lambda x: "'" + x + "'", SEXO)), ')'))

        if len(TIPO_VISTO) > 0:
            where += ''.join(('| TIPO_VISTO IN(', ', '.join(map(lambda x: "'" + x + "'", TIPO_VISTO)), ')'))

        if len(TIPO_MOVIMENTO) > 0:
            where += ''.join(('| TIPO_MOVIMENTO IN(', ', '.join(map(lambda x: "'" + x + "'", TIPO_MOVIMENTO)), ')'))

        if len(TIPOLOGIA_EXTRATOR) > 0:
            where += ''.join(('| TIPOLOGIA_EXTRATOR IN(', ', '.join(map(lambda x: "'" + x + "'", TIPOLOGIA_EXTRATOR)), ')'))

        if len(ADMITIDOS_DESLIGADOS) > 0:
            where += ''.join(('| ADMITIDOS_DESLIGADOS IN(', ', '.join(map(lambda x: "'" + x + "'", ADMITIDOS_DESLIGADOS)), ')'))


        if len(where) > 0:
            where = ''.join((' where ', where[2:].replace('|', ' AND')))

        table = table.replace('rb_', 'tb_')

        toProceed = self.__checkFilters(series[0], table, where, 
            ANO = ANO , 
            MES = MES, 
            UF = UF, 
            MUNICIPIO = MUNICIPIO, 
            CONTINENTE = CONTINENTE, 
            PAIS = PAIS, 
            SEXO = SEXO, 
            TIPO_VISTO = TIPO_VISTO, 
            TIPOLOGIA_EXTRATOR = TIPOLOGIA_EXTRATOR, 
            TIPO_MOVIMENTO = TIPO_MOVIMENTO, 
            ADMITIDOS_DESLIGADOS = ADMITIDOS_DESLIGADOS)

        if toProceed == 0:
            _message = 'Numero de filtros não permitido'
            raise HTTPException(_message)
            return qex.throw(_message)
            # return '[[], []]'

        selectX = []
        selectSerie = []

        sql = ''.join(('SELECT DISTINCT({}) as {}, '.format(eixoX, eixoX)[0:-2], ' FROM {}'.format(table), where))

        select1 = ctx.engine.execute(sql).fetchall()

        [(selectX.append(list(row))) for row in select1]

        #

        sql = ''.join(('SELECT DISTINCT({}) as {}, '.format(series[0], series[0])[0:-2], ' FROM {}'.format(table), where))

        select2 = ctx.engine.execute(sql).fetchall()

        [(selectSerie.append(list(row))) for row in select2]

        listaFinal = []
        columns = ["'" + eixoX + "'"]

        [columns.append("'" + serie[0] + "'") for serie in selectSerie]

        # chart
        listaChart = []
        strChart = "['" + eixoX + "'"

        for row in selectSerie:
            strChart += ", '" + row[0] + "'"

        strChart += "]"

        listaChart.append(strChart)

        for item in selectX:
            str1 = ''
            strChart = ''

            for item1 in selectSerie:
                where1 = where

                where1 = ' WHERE ' if len(where) == 0 else where + ' AND '

                sql = ''.join(('SELECT COUNT(*) as {} FROM {}'.format(series[0], table), where1, 
                    "{} = '{}' AND {} = '{}'".format(eixoX, item[0], series[0], item1[0])))

                contador = ctx.engine.execute(sql).scalar()

                str1 += ', ' + str(contador)
                strChart += ', ' + str(contador)

            listaFinal.append(["'{}'".format(item[0]) + str1])
            listaChart.append("['{}'".format(item[0]) + strChart + "]")

        retorno = []
        retorno.append(super().toJson([columns, listaFinal]))
        retorno.append('[' + ', '.join(listaChart) + ']')

        return super().toJson(retorno)

    def viewChart(self, ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, SEXO, TIPO_VISTO, TIPOLOGIA_EXTRATOR, TIPO_MOVIMENTO, ADMITIDOS_DESLIGADOS, table,
                  eixoX, series):
        """ 
        Retorna dados para popular o chart
        Eixo X: ANO por exemplo e várias Series: PAIS, CONTINENTE, SEXO
        """
        table = table.lower()
        where = ''

        if len(ANO) > 0:
            where += ''.join(('| ANO IN(', ', '.join(map(str, ANO)), ')'))

        if len(MES) > 0:
            where += ''.join(('| MES IN(', ', '.join(map(lambda x: "'" + x + "'", MES)), ')'))

        if len(CONTINENTE) > 0:
            where += ''.join(('| CONTINENTE IN(', ', '.join(map(lambda x: "'" + x + "'", CONTINENTE)), ')'))

        if len(PAIS) > 0:
            where += ''.join(('| PAIS IN(', ', '.join(map(lambda x: "'" + x + "'", PAIS)), ')'))

        if len(UF) > 0:
            where += ''.join(('| UF IN(', ', '.join(map(lambda x: "'" + x + "'", UF)), ')'))

        if len(MUNICIPIO) > 0:
            where += ''.join(('| MUNICIPIO IN(', ', '.join(map(lambda x: "'" + x + "'", MUNICIPIO)), ')'))

        if len(SEXO) > 0:
            where += ''.join(('| SEXO IN(', ', '.join(map(lambda x: "'" + x + "'", SEXO)), ')'))

        if len(where) > 0:
            where = ''.join((' where ', where[2:].replace('|', ' AND')))

        table = table.replace('rb_', 'tb_')

        toProceed = self.__checkFilters(series[0], table, where, 
            ANO = ANO , 
            MES = MES, 
            UF = UF, 
            MUNICIPIO = MUNICIPIO, 
            CONTINENTE = CONTINENTE, 
            PAIS = PAIS, 
            SEXO = SEXO, 
            TIPO_VISTO = TIPO_VISTO, 
            TIPOLOGIA_EXTRATOR = TIPOLOGIA_EXTRATOR, 
            TIPO_MOVIMENTO = TIPO_MOVIMENTO, 
            ADMITIDOS_DESLIGADOS = ADMITIDOS_DESLIGADOS)

        if toProceed == 0:
            return qex.throw('Numero de filtros não permitidos')
            #return '[]'

        selectX = []
        selectSerie = []

        sql = ''.join(('SELECT DISTINCT({}) as {}, '.format(eixoX, eixoX)[0:-2], ' FROM {}'.format(table), where))

        select1 = ctx.engine.execute(sql).fetchall()

        [(selectX.append(list(row))) for row in select1]

        #

        sql = ''.join(('SELECT DISTINCT({}) as {}, '.format(series[0], series[0])[0:-2], ' FROM {}'.format(table), where))

        select2 = ctx.engine.execute(sql).fetchall()

        [(selectSerie.append(list(row))) for row in select2]

        listaFinal = []

        str1 = "['" + eixoX + "'"

        for row in selectSerie:
            str1 += ", '" + row[0] + "'"

        str1 += "]"

        listaFinal.append(str1)

        for item in selectX:
            str1 = ''

            for item1 in selectSerie:
                where1 = where

                where1 = ' WHERE ' if len(where) == 0 else where + ' AND '

                sql = ''.join(('SELECT COUNT(*) as {} FROM {}'.format(series[0], table), where1, 
                    "{} = '{}' AND {} = '{}'".format(eixoX, item[0], series[0], item1[0])))

                contador = ctx.engine.execute(sql).scalar()

                str1 += ', ' + str(contador)

            listaFinal.append("['{}'".format(item[0]) + str1 + "]")

        return '[' + ', '.join(listaFinal) + ']'

    def downloadContent(self, ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, SEXO, TIPO_VISTO, TIPOLOGIA_EXTRATOR, TIPO_MOVIMENTO, ADMITIDOS_DESLIGADOS, 
        table, eixoX, series, pathName):

        data = self.viewChart(ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, SEXO, TIPO_VISTO, TIPOLOGIA_EXTRATOR, TIPO_MOVIMENTO, ADMITIDOS_DESLIGADOS, table,
            eixoX, series)

        fileName = 'datax{}.csv'.format(str(datetime.now().microsecond))

        path = '/'.join((pathName, fileName))

        for item in ['[[', ']]', '], [', "'"]:
            data = data.replace(item, '\n') if item in ['], ['] else data.replace(item, '')

        with open(path, 'w') as f:
            f.write(data)
            f.close()

        return json.dumps({ 'status': 'OK', 'link': fileName })

    def __checkFilters(self, field, table, where, **kwargs):
        
        sql = ''.join(('SELECT COUNT(DISTINCT({})) as {}, '.format(field, field)[0: -2], ' FROM {}'.format(table), where))

        distinct = ctx.engine.execute(sql).scalar()

        numParams = 0
        retorno = 1

        for key, value in kwargs.items(): 
            if key == field:
                numParams = len(value)

        if distinct > 5 and numParams == 0:
            retorno = 0
        elif numParams > 5:
            retorno = 0

        return retorno

    def __getFieldsOfTable(self, tableName):
        fields = []

        [fields.append(field) for field in dir(tableName) if not field.startswith('_')]

        return fields

    def getTables(self):
        rows = []
        classes = []
        
        classes.append((mapCTPS(0, '', '', '', '', '', '', ''), mapCTPS.__name__))
        classes.append((mapCGIL(0, '', '', '', '', '', '', ''), mapCGIL.__name__))
        classes.append((mapCAGED(0, '', '', '', '', '', '', '', ''), mapCAGED.__name__))
        classes.append((mapRAIS(0, '', '', '', '', '', ''), mapRAIS.__name__))
        classes.append((mapSISMIGRA_ENTRADA(0, '', '', '', '', '', '', '', ''), mapSISMIGRA_ENTRADA.__name__))
        classes.append((mapSISMIGRA_REGISTRO(0, '', '', '', '', '', '', '', ''), mapSISMIGRA_REGISTRO.__name__))
        classes.append((mapSTI(0, '', '', '', '', '', '', '', '', ''), mapSTI.__name__))

        [rows.append({ table[1]: self.__getFieldsOfTable(table[0]) }) for table in classes]

        return rows

    def __executeQuery(self, sql, field):
        select1 = ctx.engine.execute(sql)
        num = str(len(list(select1)))

        return "['{}', ".format(field) + num + ", '{}' ]".format(num + ' (' + field + ')')

    def __close(self):
        try:
            ctx.session.close()
            ctx.conn.close()
        except:
            pass
    
    def __del__(self):
        self.__close()

class myLists():

    def __init__(self):
        pass

    def aboutListComprehenssion(self):

        aThousand = range(1, 1001)

        print(('aThousand is: ' ,type(aThousand)))
        print(len(aThousand))

        filteredByFilter = filter(lambda x: x % 2 == 0, aThousand)
        filteredByIter = [x for x in aThousand if x % 2 == 0]

        pairs = list(filteredByFilter)

        print(('filteredByFilter is: ', type(filteredByFilter), ' - Number of records: ', len(pairs)))
        print(('filteredByIter is: ', type(filteredByIter), ' - Number of records: ', len(list(filteredByIter))))

        print('-' * 50)

        # [item * 2 for item in pairs] # Wrong way

        for i, item in enumerate(pairs): # Right way
            item = item * 2

        print(pairs[0:10])


    def basicConcepts(self):

        # o que posso armazenar em uma variável (caixinha)??

        goal = 'Meta para 2019: aprender python e data analisis' # uma frase

        Year = 2019 # 1 numero

        dict1 = {'Goal': 'Meta para 2019: aprender python e data analisis', 'Ano': 2019 } # 1 dicionário
        print(dict1)

        dict2 = {'Goal': goal, 'Ano': Year} # o mesmo dicionário com variáveis
        print(dict2)

        NumOfWordsInMyGoal = goal.split(' ') # crio uma lista com cada palavra de minha frase

        for word in NumOfWordsInMyGoal: # iteração por lsta
            print(word)

        # ou 

        [print(word) for word in NumOfWordsInMyGoal] # iteração por list comprehenssion
