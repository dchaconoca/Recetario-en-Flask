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

def create_app(settings_module='config.DevelopmentConfig'):
    app = Flask(__name__)

    app.config.from_object(settings_module)

    # Se agregó "pymysql" para que funcionara, pues por defecto utiliza mysqlclient
    # que me da un error al instalarlo, aparentemente no funciona en 32 bits

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