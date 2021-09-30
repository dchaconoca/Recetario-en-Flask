#########################################################
# ENTRADA DEL PROYECTO FLASK
#########################################################

from app import create_app
import os

settings_module = os.getenv('APP_SETTINGS_MODULE')

if not settings_module:
    settings_module = 'config.DevelopmentConfig'

print("settings_module", settings_module)

app = create_app(settings_module)
app.run()



