#########################################################
# VISTAS DEL BLUEPRINT REFERENCIAL
#########################################################

from flask import Flask, redirect, url_for, render_template, flash
from flask import request

# Blueprint
from . import referencial_bp

# Otros módulos
from .models import Categoria, Medida


# Para definir las vistas, se usa el Blueprint para el decorador route
# y no la app como normalmente
# @app.route(...: Se reemplaza @app por @referencial_bp

#########################################################
# VISTAS PARA LAS CATEGORIAS
#########################################################

# Lista de todas las categorias de recetas
@referencial_bp.route('/referencial/lista_categorias')
def ListaCategorias():
    categorias = Categoria.listar()
    return render_template('/referencial/categoria_list.html', categorias = categorias)

# Consulta una categoria de recetas dada
# El parámetro acción permite "adaptar" el template
@referencial_bp.route('/referencial/consultar_categoria/<id>')
def ConsultarCategoria(id):
    accion = "Consultar"
    categoria = Categoria()
    unaCategoria = categoria.buscar(id)
    return render_template('/referencial/categoria_detail.html', categoria=unaCategoria, accion=accion)

# Crea una categoria de recetas 
# El parámetro acción permite "adaptar" el template
@referencial_bp.route('/referencial/crear_categoria', methods=["GET", "POST"])
def CrearCategoria():
    accion = "Crear"
    categoria = Categoria()
    if request.method == 'POST':
        categoria.nombre = request.form['nombre']
        categoria.descripcion = request.form['descripcion']

        if categoria.validar():                     
            categoria.guardar()
            mensaje="Categoria " + categoria.nombre + " creada satisfactoriamente" 
            flash(mensaje)
            return redirect(url_for('referencial.ListaCategorias'))
              
    return render_template('/referencial/categoria_detail.html', categoria=categoria, accion=accion)

# Edita una categoria de recetas dada
# El parámetro acción permite "adaptar" el template
@referencial_bp.route('/referencial/editar_categoria/<int:id>',  methods=["GET", "POST"])
def EditarCategoria(id):
    accion = "Editar"
    categoria = Categoria()
    unaCategoria = categoria.buscar(id)

    if request.method == 'POST':
        categoria.id = id
        categoria.nombre = request.form['nombre']
        categoria.descripcion = request.form['descripcion']

        if categoria.validar():   
            categoria.guardar()
            mensaje="Categoria " + categoria.nombre + " modificada satisfactoriamente" 
            flash(mensaje)
            return redirect(url_for('referencial.ListaCategorias'))

    return render_template('/referencial/categoria_detail.html', categoria=unaCategoria, accion=accion)


# Elimina una categoria de recetas dada
@referencial_bp.route('/referencial/eliminar_categoria/<int:id>')
def EliminarCategoria(id):
    categoria = Categoria()
    if categoria.borrar(id):
        flash('Categoria eliminada satisfactoriamente')
    
    return redirect(url_for('referencial.ListaCategorias'))


#########################################################
# VISTAS PARA LAS UNIDADES DE MEDIDA
#########################################################

# Lista de todas las unidades de medida
@referencial_bp.route('/referencial/lista_medidas')
def ListaMedidas():
    medidas = Medida.listar()
    return render_template('/referencial/medida_list.html', medidas = medidas)

# Consulta una unidad de medida dada
# El parámetro acción permite "adaptar" el template
@referencial_bp.route('/referencial/consultar_medida/<id>')
def ConsultarMedida(id):
    accion = "Consultar"
    medida = Medida()
    unaMedida = medida.buscar(id)
    return render_template('/referencial/medida_detail.html', medida=unaMedida, accion=accion)

# Crea una unidad de medida
# El parámetro acción permite "adaptar" el template
@referencial_bp.route('/referencial/crear_medida', methods=["GET", "POST"])
def CrearMedida():
    accion = "Crear"
    medida = Medida()
    if request.method == 'POST':
        medida.nombre = request.form['nombre']
        medida.proporcion = request.form['proporcion']

        if medida.validar():                     
            medida.guardar()
            mensaje="Unidad de medida " + medida.nombre + " creada satisfactoriamente" 
            flash(mensaje)
            return redirect(url_for('referencial.ListaMedidas'))
              
    return render_template('/referencial/medida_detail.html', medida=medida, accion=accion)

# Edita una unidad de medida
# El parámetro acción permite "adaptar" el template
@referencial_bp.route('/referencial/editar_medida/<int:id>',  methods=["GET", "POST"])
def EditarMedida(id):
    accion = "Editar"
    medida = Medida()
    unaMedida = medida.buscar(id)

    if request.method == 'POST':
        medida.id = id
        medida.nombre = request.form['nombre']
        medida.proporcion = request.form['proporcion']

        if medida.validar():   
            medida.guardar()
            mensaje="Unidad de medida " + medida.nombre + " modificada satisfactoriamente" 
            flash(mensaje)
            return redirect(url_for('referencial.ListaMedidas'))

    return render_template('/referencial/medida_detail.html', medida=unaMedida, accion=accion)


# Elimina una unidad de medida
@referencial_bp.route('/referencial/eliminar_medida/<int:id>')
def EliminarMedida(id):
    medida = Medida()
    if medida.borrar(id):
        flash('Unidad de mdida eliminada satisfactoriamente')
    
    return redirect(url_for('referencial.ListaMedidas'))




