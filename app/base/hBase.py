import app.base.Cifra as Cifra
import app.base.QException as ex
import datetime
import json
from decimal import Decimal

class hBase:

    def __init__(self, keep=None):
        try:
            cdate = Cifra.decifra(keep)
            datetime.datetime.strptime(cdate, '%d-%m-%Y %H:%M:%S')

        except Exception:
            raise Exception('Acesso inválido...')

    def threatColunms(self, row):
        isStr = type(row) is str

        if not isStr:
            retorno = list(row)

            for i, item in enumerate(retorno):
                if type(retorno[i]) == str:
                    retorno[i] = retorno[i].replace('"', '') 
                elif type(retorno[i]) == int:
                    pass
                elif type(retorno[i]) == Decimal:
                    retorno[i] = float(item)
        elif isStr:
            retorno = row.replace('"', '') 

        return retorno

    def toJson(self, lista):
        lista1 = []

        lista1.extend(list(map(self.threatColunms, lista)))

        return json.dumps(lista1)

    def toDict(self, lista):
        dict1 = []

        for item in lista:
            dict1.append(item._asdict())

        return dict1

    def queryToDict(self, query):

        dict1 = []

        for item in query:
            dict1.append(item._asdict())

        return str(dict1)

    def TrataDataHora(self, dt1=None):
        if dt1 is None:
            dt1 = datetime.datetime.today()

        retorno = "{0}-{1}-{2} {3}:{4}:{5}".format(str(dt1.day).rjust(2, '0'),
            str(dt1.month).rjust(2, '0'), str(dt1.year),
            str(dt1.hour).rjust(2, '0'), str(dt1.minute).rjust(2, '0'),
            str(dt1.second).rjust(2, '0'))

        return retorno
