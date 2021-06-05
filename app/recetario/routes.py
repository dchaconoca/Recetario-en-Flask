#########################################################
# VISTAS DEL BLUEPRINT RECETARIO
#########################################################

from flask import Flask, redirect, url_for, render_template, flash
from flask import request

# Blueprint
from . import recetario_bp

# Otros módulos
from .models import Ingrediente, Receta
from app.referencial.models import Medida, Categoria


#########################################################
# VISTAS PARA LOS INGREDIENTES
#########################################################

# Lista de todos los ingredientes
@recetario_bp.route('/recetario/lista_ingredientes')
def ListaIngredientes():
    ingredientes = Ingrediente.listar()
    return render_template('/recetario/ingrediente_list.html', ingredientes = ingredientes)

# Consulta un ingrediente dado
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/consultar_ingrediente/<id>')
def ConsultarIngrediente(id):
    accion = "Consultar"
    ingrediente = Ingrediente()
    unIngrediente = ingrediente.buscar(id)

    medidas = Medida.listar()

    return render_template('/recetario/ingrediente_detail.html', ingrediente=unIngrediente, medidas=medidas, accion=accion)

# Crea un ingrediente
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/crear_ingrediente', methods=["GET", "POST"])
def CrearIngrediente():
    accion = "Crear"
    ingrediente = Ingrediente()

    medidas = Medida.listar()

    if request.method == 'POST':
        ingrediente.nombre = request.form['nombre']
        ingrediente.descripcion = request.form['descripcion']
        ingrediente.precio = request.form['precio']
        ingrediente.medida_id = request.form['medida_id']
        
        if ingrediente.validar():                     
            ingrediente.guardar()
            mensaje="Ingrediente " + ingrediente.nombre + " creado satisfactoriamente" 
            flash(mensaje)
            return redirect(url_for('recetario.ListaIngredientes'))
              
    return render_template('/recetario/ingrediente_detail.html', ingrediente=ingrediente, medidas=medidas, accion=accion)

# Edita un ingrediente
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/editar_ingrediente/<int:id>',  methods=["GET", "POST"])
def EditarIngrediente(id):
    accion = "Editar"
    ingrediente = Ingrediente()
    unIngrediente = ingrediente.buscar(id)

    medidas = Medida.listar()

    if request.method == 'POST':
        ingrediente.id = id
        ingrediente.nombre = request.form['nombre']
        ingrediente.descripcion = request.form['descripcion']
        ingrediente.precio = request.form['precio']
        ingrediente.medida_id = request.form['medida_id']

        if ingrediente.validar():  
            ingrediente.guardar()
            mensaje="Ingrediente " + ingrediente.nombre + " modificado satisfactoriamente" 
            flash(mensaje)
            return redirect(url_for('recetario.ListaIngredientes'))

    return render_template('/recetario/ingrediente_detail.html', ingrediente=unIngrediente, medidas=medidas, accion=accion)


# Elimina una unidad de medida
@recetario_bp.route('/recetario/eliminar_ingrediente/<int:id>')
def EliminarIngrediente(id):
    ingrediente = Ingrediente()
    if ingrediente.borrar(id):
        flash('Ingrediente eliminado satisfactoriamente')
    
    return redirect(url_for('recetario.ListaIngredientes'))



#########################################################
# VISTAS PARA LAS RECETAS
#########################################################

# Lista de todas las recetas
@recetario_bp.route('/recetario/lista_recetas')
def ListaRecetas():
    recetas = Receta.listar()
    return render_template('/recetario/receta_list.html', recetas = recetas)

# Consulta una receta dada
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/consultar_receta/<id>')
def ConsultarReceta(id):
    accion = "Consultar"
    receta = Receta()
    unaReceta = receta.buscar(id)

    categorias = Categoria.listar()

    medidas = Medida.listar()

    ingredentes = Ingrediente.listar()

    return render_template('/recetario/receta_detail.html', receta=unaReceta, categorias=categorias, accion=accion)

# Crea una receta
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/crear_receta', methods=["GET", "POST"])
def CrearReceta():
    accion = "Crear"
    receta = Receta()

    categorias = Categoria.listar()

    if request.method == 'POST':
        receta.titulo = request.form['titulo']
        receta.descripcion = request.form['descripcion']
        receta.precio_venta = request.form['precio_venta']
        receta.categoria_id = request.form['categoria_id']

        if receta.validar():                     
            receta.guardar()
            mensaje="Receta " + receta.titulo + " creada satisfactoriamente" 
            flash(mensaje)
            return redirect(url_for('recetario.ListaRecetas'))
              
    return render_template('/recetario/receta_detail.html', receta=receta, categorias=categorias, accion=accion)

# Edita una receta
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/editar_receta/<int:id>',  methods=["GET", "POST"])
def EditarReceta(id):
    accion = "Editar"
    receta = Receta()
    unaReceta = receta.buscar(id)

    categorias = Categoria.listar()

    if request.method == 'POST':
        receta.id = id
        receta.titulo = request.form['titulo']
        receta.descripcion = request.form['descripcion']
        receta.precio_venta = request.form['precio_venta']
        receta.categoria_id = request.form['categoria_id']

        if receta.validar():   
            receta.guardar()
            mensaje="Receta " + receta.titulo + " modificada satisfactoriamente" 
            flash(mensaje)
            return redirect(url_for('recetario.ListaRecetas'))

    return render_template('/recetario/receta_detail.html', receta=unaReceta, categorias=categorias, accion=accion)


# Elimina una receta
@recetario_bp.route('/recetario/eliminar_receta/<int:id>')
def EliminarReceta(id):
    receta = Receta()
    if receta.borrar(id):
        flash('Receta eliminada satisfactoriamente')
    
    return redirect(url_for('recetario.ListaRecetas'))






