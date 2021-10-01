#########################################################
# ENTRADA DEL PROYECTO FLASK
#########################################################

from app import create_app
import os

settings_module = os.getenv('APP_SETTINGS_MODULE')

if not settings_module:
    settings_module = 'config.DevelopmentConfig'

# print("settings_module", settings_module)

app = create_app(settings_module)

if __name__ == '__main__':
    app.run()

# port = int(os.environ.get('PORT', 5000))
# app.run(host='0.0.0.0', port=port)


