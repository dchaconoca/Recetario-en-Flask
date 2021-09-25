#########################################################
# INICIALIZACIÓN DE LA APP
# Configuraciones varias
# Declaración de la BD y herramientas para migrar
# Registro de los Blueprints de la aplicación
#########################################################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from flask_migrate import Migrate

from decouple import config as config_decouple

db = SQLAlchemy()
migrate = Migrate()

def create_app(enviroment):

    app = Flask(__name__)

    app.config['SECRET_KEY'] = '84309ejf02934jrm34urp34urn34ur'

    app.config.from_object(enviroment)

    # Se agregó "pymysql" para que funcionara, pues por defecto utiliza mysqlclient
    # que me da un error al instalarlo, aparentemente no funciona en 32 bits
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://diana:Color74@localhost/ProyectoFlask?charset=utf8mb4'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)

    # Registro de Blueprints
    from .public import public_bp
    app.register_blueprint(public_bp)

    from .referencial import referencial_bp
    app.register_blueprint(referencial_bp)

    from .recetario import recetario_bp
    app.register_blueprint(recetario_bp)

    return app



