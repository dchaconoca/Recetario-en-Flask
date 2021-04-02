#########################################################
# INICIALIZACIÓN DE LA APP
# Configuraciones varias
# Declaración de la BD y herramientas para migrar
# Registro de los Blueprints de la aplicación
#########################################################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

    # Se agregó "pymysql" para que funcionara, pues por defecto utiliza mysqlclient
    # que me da un error al instalarlo, aparentemente no funciona en 32 bits
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dchaconoca:Diana-2074@localhost/ProyectoFlask?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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





