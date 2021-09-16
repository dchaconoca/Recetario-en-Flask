#########################################################
# INICIALIZACIÓN DEL PAQUETE PUBLIC
# Definición del Blueprint
#########################################################

from flask import Blueprint

# Recetas: Nombre del Blueprint
# __name__: Importa el nombre del módulo
# Nombres de los directorios de los templates y los archivos static

public_bp = Blueprint('public', __name__, template_folder='templates', static_folder='static')

# Importa todas las vistas de módulo para que la app sea conciente de de que existen
from . import routes