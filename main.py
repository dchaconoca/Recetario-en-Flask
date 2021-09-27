#########################################################
# ENTRADA DEL PROYECTO FLASK
#########################################################

from app import create_app
from decouple import config as config_decouple

enviroment = config['development']

if config_decouple('PRODUCTION', default=False):
    enviroment = config['production']

app = create_app(enviroment)

app.run



