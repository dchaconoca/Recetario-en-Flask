# from decouple import config

class Config:
    SECRET_KEY = 'fjaf343efwereb1g5eere5rhrtery'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://diana:Color74@localhost/ProyectoFlask?charset=utf8mb4'
    DEBUG = True

class ProductionConfig(Config):
    #SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='localhost')
    SQLALCHEMY_DATABASE_URI ='postgresql://gxedmqdfuiwtfg:e181db08b929e912e1f41708f6801f16601b253670cd9ca43a7f2a8ac4d93a5c@ec2-54-174-172-218.compute-1.amazonaws.com:5432/db74dnhp8cakq2'

