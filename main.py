#########################################################
# ENTRADA DEL PROYECTO FLASK
#########################################################

from app import create_app
import os

settings_module = os.getenv('APP_SETTINGS_MODULE')

if not settings_module:
    settings_module = 'config.DevelopmentConfig'

app = create_app(settings_module)

if __name__ == '__main__':
    app.run()



