from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import String, Table, Integer, Numeric, DateTime, BLOB
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper
import json
from app.base.mapTable import mapUsuario, mapFile, mapCTPS, mapCAGED, mapCGIL, mapRAIS, mapSISMIGRA_ENTRADA, mapSISMIGRA_REGISTRO, mapSTI, mapTEMP
import datetime
from decimal import Decimal
import app.base.Cifra 
from venv.config import DevelopmentConfig as config

# db_host = '10.10.28.11'
# db_user = 'sisdesenv'
# db_pass = 'mj@bdd'
# db_name = 'datamigra'
# db_root = 'mysql+pymysql://%s:%s@%s:3306/%s' % (db_user, db_pass, db_host, db_name)

strConn = ''.join((config.DB_USERNAME, ':', config.DB_PASSWORD, '@', config.DB_SERVER_NAME, '/', config.DB_NAME))

engine = create_engine('mysql+pymysql://' + strConn, isolation_level="READ UNCOMMITTED")
# engine = create_engine('mysql+pymysql://root:56Runna01@localhost:3306/datamigra', isolation_level="READ UNCOMMITTED")
# engine = create_engine('postgresql+psycopg2://postgres:56Runna01@localhost:5432/DataMigra', isolation_level="READ UNCOMMITTED")

metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()

tables = []

usuario = Table('tb_usuario', metadata,
    Column('ID_USUARIO', Integer, primary_key=True, autoincrement='auto'),
    Column('NOME_USUARIO', String(60), nullable=False),
    Column('SENHA_USUARIO', String(150), nullable=True),
    Column('EMAIL_USUARIO', String(100), nullable=True),
    Column('USUARIO_ATIVO', Numeric, nullable=True),
    Column('TIPO_USUARIO', Integer, nullable=True))

file = Table('tb_file', metadata,
    Column('ID_FILE', Integer, primary_key=True, autoincrement='auto'),
    Column('FILE_NAME', String(120), nullable=True),
    Column('DATE_FILE', DateTime, nullable=True),
    Column('CONTENT_FILE', BLOB, nullable=True))

ctps = Table('tb_ctps', metadata,
    Column('ID_CTPS', Integer, primary_key=True, autoincrement='auto'),
    Column('ANO', String(4), nullable=True),
    Column('MES', String(50), nullable=True),
    Column('UF', String(50), nullable=True),
    Column('MUNICIPIO', String(100), nullable=True),
    Column('PAIS', String(100), nullable=True),
    Column('CONTINENTE', String(50), nullable=True),
    Column('SEXO', String(50), nullable=True))

caged = Table('tb_caged', metadata,
    Column('ID_CAGED', Integer, primary_key=True, autoincrement='auto'),
    Column('ANO', String(4), nullable=True),
    Column('MES', String(50), nullable=True),
    Column('UF', String(20), nullable=True),
    Column('MUNICIPIO', String(100), nullable=True),
    Column('PAIS', String(100), nullable=True),
    Column('CONTINENTE', String(50), nullable=True),
    Column('ADMITIDOS_DESLIGADOS', String(20), nullable=True),
    Column('SEXO', String(50), nullable=True))

cgil = Table('tb_cgil', metadata,
    Column('ID_CGIL', Integer, primary_key=True, autoincrement='auto'),
    Column('ANO', String(4), nullable=True),
    Column('MES', String(50), nullable=True),
    Column('UF', String(20), nullable=True),
    Column('PAIS', String(100), nullable=True),
    Column('CONTINENTE', String(50), nullable=True),
    Column('TIPO_VISTO', String(50), nullable=True),
    Column('SEXO', String(50), nullable=True))

rais = Table('tb_rais', metadata,
    Column('ID_RAIS', Integer, primary_key=True, autoincrement='auto'),
    Column('ANO', String(4), nullable=True),
    Column('UF', String(20), nullable=True),
    Column('MUNICIPIO', String(100), nullable=True),
    Column('PAIS', String(100), nullable=True),
    Column('CONTINENTE', String(50), nullable=True),
    Column('SEXO', String(50), nullable=True))

sismigra_entrada = Table('tb_sismigra_entrada', metadata,
    Column('ID_MIGRA', Integer, primary_key=True, autoincrement='auto'),
    Column('ANO', String(4), nullable=True),
    Column('MES', String(50), nullable=True),
    Column('UF', String(20), nullable=True),
    Column('MUNICIPIO', String(100), nullable=True),
    Column('PAIS', String(100), nullable=True),
    Column('CONTINENTE', String(50), nullable=True),
    Column('TIPOLOGIA_ENTRADA', String(50), nullable=True),
    Column('SEXO', String(50), nullable=True))

sismigra_registro = Table('tb_sismigra_registro', metadata,
    Column('ID_MIGRA', Integer, primary_key=True, autoincrement='auto'),
    Column('ANO', String(4), nullable=True),
    Column('MES', String(50), nullable=True),
    Column('UF', String(20), nullable=True),
    Column('MUNICIPIO', String(100), nullable=True),
    Column('PAIS', String(100), nullable=True),
    Column('CONTINENTE', String(50), nullable=True),
    Column('TIPOLOGIA_ENTRADA', String(50), nullable=True),
    Column('SEXO', String(50), nullable=True))

sti = Table('tb_sti', metadata,
    Column('ID_STI', Integer, primary_key=True, autoincrement='auto'),
    Column('ANO', String(4), nullable=True),
    Column('MES', String(50), nullable=True),
    Column('UF', String(20), nullable=True),
    Column('PAIS', String(100), nullable=True),
    Column('CONTINENTE', String(50), nullable=True),
    Column('TIPO_MOVIMENTO', String(50), nullable=True),
    Column('TIPOLOGIA_ENTRADA', String(50), nullable=True),
    Column('SEXO', String(50), nullable=True))

temp = Table('tb_temp', metadata,
    Column('ID_TEMP', Integer, primary_key=True, autoincrement='auto'),
    Column('MILISEC', Integer, nullable=True),
    Column('TABELA_ORIGEM', String(20), nullable=True),
    Column('ANO', String(4), nullable=True))

tables.append([mapUsuario, usuario])
tables.append([mapFile, file])
tables.append([mapCTPS, ctps])
tables.append([mapCAGED, caged])
tables.append([mapCGIL, cgil])
tables.append([mapRAIS, rais])
tables.append([mapSISMIGRA_ENTRADA, sismigra_entrada])
tables.append([mapSISMIGRA_REGISTRO, sismigra_registro])
tables.append([mapSTI, sti])
tables.append([mapTEMP, temp])

def mapAllTables():

    [mapper(table[0], table[1]) for table in tables]

def connect():
    try:
        return engine.connect()
    except Exception:
        raise Exception('Não foi possível conectar no banco de dados')

def close():
    try:
        engine.close()
    except Exception:
        pass

conn = connect()
mapAllTables()

# from unittest import TestCase, main

# class testDatabase(TestCase):

#     def testConnection(self):
#         assert connect() == conn

# testDatabase().testConnection()
