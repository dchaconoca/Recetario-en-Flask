#########################################################
# VISTAS DEL BLUEPRINT PUBLIC
#########################################################

from flask import render_template

# Blueprint
from . import public_bp

@public_bp.route('/')
def home():
    return render_template('/public/home.html')

@public_bp.route('/quien')
def quien():
    return render_template('/public/quien.html')

@public_bp.route('/contacto')
def contacto():
    return render_template('/public/contacto.html')