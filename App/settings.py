

class Config():
    DEBUG = False
    TESTING = False
    SECRET = 'rrr'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def getMYSQLURI(DATABASE):
    USER = DATABASE.get("USER")
    PASSWORD = DATABASE.get("PASSWORD")
    HOST = DATABASE.get("HOST")
    PORT = DATABASE.get("PORT")
    NAME = DATABASE.get("NAME")

    return "mysql+pymysql://{}:{}@{}:{}/{}".format(USER,PASSWORD,HOST,PORT,NAME)

def getSQLITEURI(NANE):

    return "sqlite:///{}.db".format(NANE)


class DevelopConfig(Config):
    DEBUG = True
    NAME = 'sqlite'

    SQLALCHEMY_DATABASE_URI = getSQLITEURI(NAME)


class TestingConfig(Config):
    TESTING = True
    NAME = 'sqlite'

    SQLALCHEMY_DATABASE_URI = getSQLITEURI(NAME)


class StagingConfig(Config):
    NAME = 'sqlite'

    SQLALCHEMY_DATABASE_URI = getSQLITEURI(NAME)


class ProductConfig(Config):
    NAME = 'sqlite'

    SQLALCHEMY_DATABASE_URI = getSQLITEURI(NAME)


env = {
    "develop":DevelopConfig,
    "testing":TestingConfig,
    "staging":StagingConfig,
    "product":ProductConfig,
    "default":DevelopConfig
}





