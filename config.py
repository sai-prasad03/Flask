class Config(object):

    SECRET_KEY = 'SBDBKJKFKN'
    SQLALCHEMY_DATABASE_URI = "mysql://root:1234@localhost/ss"
    SQLALCHEMY_TRACK_MODIFICATION = False

class Developmentconfig(Config):

    SQLALCHEMY_ECHO = True
    DEBUG = True


app_config = {'development':Developmentconfig}