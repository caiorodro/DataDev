
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    DB_SERVER_NAME = "198.199.76.59:3306"
    DB_NAME = "Datamigra"
    DB_USERNAME = "admin"
    DB_PASSWORD = "xRun"

    ZIP_UPLOADS = "/Users/caioDoran/Documents/Projects/DataDev/csv"
    ZIP_DOWNLOADS = '/Users/caioDoran/Documents/Projects/DataDev/csv'
    #ZIP_ADDRESS = 'http://198.199.76.59/csv/'
    ZIP_ADDRESS = 'http://127.0.0.1:5000/csv/'

    SESSION_COOKIE_SECURE = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    DB_SERVER_NAME = "localhost:3306"
    DB_NAME = "Datamigra"
    DB_USERNAME = "root"
    DB_PASSWORD = "xRun"

    ZIP_UPLOADS = "/Users/caioDoran/Documents/Projects/DataDev/csv"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    DB_SERVER_NAME = "198.199.76.59:3306"
    DB_NAME = "Datamigra"
    DB_USERNAME = "root"
    DB_PASSWORD = "xRun"

    SESSION_COOKIE_SECURE = False
