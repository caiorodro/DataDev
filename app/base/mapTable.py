class mapUsuario(object):
    def __init__(self, ID_USUARIO, NOME_USUARIO, SENHA_USUARIO, EMAIL_USUARIO, USUARIO_ATIVO, TIPO_USUARIO):
        self.ID_USUARIO = ID_USUARIO
        self.NOME_USUARIO = NOME_USUARIO
        self.SENHA_USUARIO = SENHA_USUARIO
        self.EMAIL_USUARIO = EMAIL_USUARIO
        self.USUARIO_ATIVO = USUARIO_ATIVO
        self.TIPO_USUARIO = TIPO_USUARIO

class mapFile(object):
    def __init__(self, ID_FILE, FILE_NAME, DATE_FILE, CONTENT_FILE):
        self.ID_FILE = ID_FILE
        self.FILE_NAME = FILE_NAME
        self.DATE_FILE = DATE_FILE
        self.CONTENT_FILE = CONTENT_FILE

class mapCTPS(object):
    def __init__(self, ID_CTPS, ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, SEXO):
        self.ID_CTPS = ID_CTPS
        self.ANO = ANO
        self.MES = MES
        self.UF = UF
        self.MUNICIPIO = MUNICIPIO
        self.PAIS = PAIS
        self.CONTINENTE = CONTINENTE
        self.SEXO = SEXO

class mapCAGED(object):
    def __init__(self, ID_CAGED, ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, ADMITIDOS_DESLIGADOS, SEXO):
        self.ID_CAGED = ID_CAGED
        self.ANO = ANO
        self.MES = MES
        self.UF = UF
        self.MUNICIPIO = MUNICIPIO
        self.PAIS = PAIS
        self.CONTINENTE = CONTINENTE
        self.ADMITIDOS_DESLIGADOS = ADMITIDOS_DESLIGADOS
        self.SEXO = SEXO

class mapCGIL(object):
    def __init__(self, ID_CGIL, ANO, MES, UF, PAIS, CONTINENTE, TIPO_VISTO, SEXO):
        self.ID_CGIL = ID_CGIL
        self.ANO = ANO
        self.MES = MES
        self.UF = UF
        self.PAIS = PAIS
        self.CONTINENTE = CONTINENTE
        self.SEXO = SEXO,
        self.TIPO_VISTO = TIPO_VISTO

class mapRAIS(object):
    def __init__(self, ID_RAIS, ANO, UF, MUNICIPIO, PAIS, CONTINENTE, SEXO):
        self.ID_RAIS = ID_RAIS
        self.ANO = ANO
        self.UF = UF
        self.MUNICIPIO = MUNICIPIO
        self.PAIS = PAIS
        self.CONTINENTE = CONTINENTE
        self.SEXO = SEXO

class mapSISMIGRA_ENTRADA(object):
    def __init__(self, ID_MIGRA, ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, TIPOLOGIA_ENTRADA, SEXO):
        self.ID_MIGRA = ID_MIGRA
        self.ANO = ANO
        self.MES = MES
        self.UF = UF
        self.MUNICIPIO = MUNICIPIO
        self.PAIS = PAIS
        self.CONTINENTE = CONTINENTE
        self.TIPOLOGIA_ENTRADA = TIPOLOGIA_ENTRADA
        self.SEXO = SEXO

class mapSISMIGRA_REGISTRO(object):
    def __init__(self, ID_MIGRA, ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, TIPOLOGIA_ENTRADA, SEXO):
        self.ID_MIGRA = ID_MIGRA
        self.ANO = ANO
        self.MES = MES
        self.UF = UF
        self.MUNICIPIO = MUNICIPIO
        self.PAIS = PAIS
        self.CONTINENTE = CONTINENTE
        self.TIPOLOGIA_ENTRADA = TIPOLOGIA_ENTRADA
        self.SEXO = SEXO

class mapSTI(object):
    def __init__(self, ID_STI, ANO, MES, UF, MUNICIPIO, PAIS, CONTINENTE, TIPO_MOVIMENTO, TIPOLOGIA_ENTRADA, SEXO):
        self.ID_STI = ID_STI
        self.ANO = ANO
        self.MES = MES
        self.UF = UF
        self.MUNICIPIO = MUNICIPIO
        self.PAIS = PAIS
        self.CONTINENTE = CONTINENTE
        self.TIPO_MOVIMENTO = TIPO_MOVIMENTO
        self.TIPOLOGIA_ENTRADA = TIPOLOGIA_ENTRADA
        self.SEXO = SEXO

class mapTEMP(object):
    def __init__(self, ID_TEMP, MILISEC, TABELA_ORIGEM, ANO):
        self.ID_TEMP = ID_TEMP
        self.MILISEC = MILISEC
        self.TABELA_ORIGEM = TABELA_ORIGEM
        self.ANO = ANO