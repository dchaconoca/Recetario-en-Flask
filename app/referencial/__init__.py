#########################################################
# INICIALIZACIÓN DEL PAQUETE REFERENCIAL
# Definición del Blueprint
#########################################################

from flask import Blueprint

# Recetas: Nombre del Blueprint
# __name__: Importa el nombre del módulo
# Nombres de los directorios de los templates y los archivos static

referencial_bp = Blueprint('referencial', __name__, template_folder='templates', static_folder='static')

# Importa todas las vistas de módulo para que la app sea conciente de de que existen
from . import routes