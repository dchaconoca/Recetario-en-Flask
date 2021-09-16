#########################################################
# VISTAS DEL BLUEPRINT RECETARIO
#########################################################

from flask import redirect, url_for, render_template, flash
from flask import request

# Blueprint
from . import recetario_bp

# Otros módulos
from .models import Ingrediente, Receta
from app.referencial.models import Medida, Categoria
from .gestion_recetas import *


#########################################################
# VISTAS PARA LOS INGREDIENTES
#########################################################

# Lista de todos los ingredientes
@recetario_bp.route('/recetario/lista_ingredientes')
def listar_ingredientes():
    ingredientes = Ingrediente.listar()
    return render_template('/recetario/ingrediente_list.html', ingredientes = ingredientes)

# Consulta un ingrediente dado
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/consultar_ingrediente/<id>')
def consultar_ingrediente(id):
    accion = "Consultar"
    ingrediente = Ingrediente()
    unIngrediente = ingrediente.buscar(id)

    medidas = Medida.listar()

    return render_template('/recetario/ingrediente_detail.html', ingrediente=unIngrediente, medidas=medidas, accion=accion)

# Crea un ingrediente
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/crear_ingrediente', methods=["GET", "POST"])
def crear_ingrediente():
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
            return redirect(url_for('recetario.listar_ingredientes'))
              
    return render_template('/recetario/ingrediente_detail.html', ingrediente=ingrediente, medidas=medidas, accion=accion)

# Edita un ingrediente
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/editar_ingrediente/<int:id>',  methods=["GET", "POST"])
def editar_ingrediente(id):
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
            return redirect(url_for('recetario.listar_ingredientes'))

    return render_template('/recetario/ingrediente_detail.html', ingrediente=unIngrediente, medidas=medidas, accion=accion)


# Elimina un ingrediente
@recetario_bp.route('/recetario/eliminar_ingrediente/<int:id>')
def eliminar_ingrediente(id):
    ingrediente = Ingrediente()
    if ingrediente.borrar(id):
        flash('Ingrediente eliminado satisfactoriamente')
    
    return redirect(url_for('recetario.listar_ingredientes'))



#########################################################
# VISTAS PARA LAS RECETAS
# Usamos el módulo gestion_recetas.py donde tratamos
# las recetas junto con sus ingredientes así como
# el cálculo de costos y precios
#########################################################

# Lista de recetas
@recetario_bp.route('/recetario/lista_recetas', methods=["GET", "POST"])
@recetario_bp.route('/recetario/lista_recetas/<int:id_cat>')
@recetario_bp.route('/recetario/lista_recetas/<int:id_ing>')
@recetario_bp.route('/recetario/lista_recetas/<int:id_cat>/<int:id_ing>')
def listar_recetas(id_cat=None, id_ing=None):
  categorias = Categoria.listar()
  ingredientes = Ingrediente.listar()

  if request.method == 'POST':
    id_cat = int(request.form['categoria_id'])
    id_ing = int(request.form['ingrediente_id'])
    recetas = lista_dinamica_recetas(id_cat, id_ing)
    return render_template('/recetario/receta_list.html', recetas=recetas, categorias=categorias, ingredientes=ingredientes, id_cat=id_cat, id_ing=id_ing)
  else:
    recetas = lista_dinamica_recetas()

  return render_template('/recetario/receta_list.html', recetas=recetas, categorias=categorias, ingredientes=ingredientes)


def contexto_receta(id):
  receta = Receta()
  una_receta = receta.buscar(id)
  # ingredientes = una_receta.ingredientes

  # # Esto funciona perfecto
  # for ingrediente in ingredientes:
  #   print(ingrediente.ingrediente_id, ingrediente.cantidad)

  contexto = {
    'receta': una_receta,
    'ingredientes': una_receta.buscar_ingredientes(),
    #'ingredientes': una_receta.ingredientes,
    'lista_ingredientes': Ingrediente.listar(),
    'medidas': Medida.listar(),
    'categorias': Categoria.listar()
  }
  return contexto
  

# Consulta una receta dada
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/consultar_receta/<int:id>')
def consultar_receta(id):
  accion = "Consultar"

  return render_template('/recetario/receta_detail.html', accion=accion, **contexto_receta(id))


# Crea una receta
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/crear_receta', methods=["GET", "POST"])
def crear_receta():
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
            return redirect(url_for('recetario.listar_recetas'))
              
    return render_template('/recetario/receta_detail.html', receta=receta, categorias=categorias, accion=accion)

# Edita una receta
# El parámetro acción permite "adaptar" el template
@recetario_bp.route('/recetario/editar_receta/<int:id>',  methods=["GET", "POST"])
def editar_receta(id):
    accion = "Editar"
    receta = Receta()

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
            return redirect(url_for('recetario.listar_recetas'))

    return render_template('/recetario/receta_detail.html', accion=accion, **contexto_receta(id))


# Elimina una receta
@recetario_bp.route('/recetario/eliminar_receta/<int:id>')
def eliminar_receta(id):
    receta = Receta()
    if receta.borrar(id):
        flash('Receta eliminada satisfactoriamente')
    
    return redirect(url_for('recetario.listar_recetas'))


#########################################################
# VISTAS PARA LOS INGREDIENTES DE UNA RECETA
#########################################################

def contexto_ingredientes_receta(id_rec):
  receta = Receta()
  una_receta = receta.buscar(id_rec)

  contexto = {
    'receta': una_receta,
    'ingredientes': una_receta.buscar_ingredientes(),
    'lista_ingredientes': Ingrediente.listar(),
    'medidas': Medida.listar()
  }
  return contexto

@recetario_bp.route('/recetario/consultar_ingredientes_receta/<int:id_rec>')
def consultar_ingredientes_receta(id_rec):
  accion = "Crear"
  return render_template('/recetario/ing_rec_detail.html', accion = accion, **contexto_ingredientes_receta(id_rec))

# Crea un ingrediente para una receta
@recetario_bp.route('/recetario/crear_ingrediente_receta/<int:id_rec>', methods=["GET", "POST"])
def crear_ingrediente_receta(id_rec):
  ingRec = IngredienteReceta()

  if request.method == 'POST':
    ingRec.receta_id = id_rec
    ingRec.ingrediente_id = request.form['ingrediente_id']
    ingRec.cantidad = request.form['cantidad']
    ingRec.medida_id = request.form['medida_id']
    
    if ingRec.validar():                     
        ingRec.guardar()
        return redirect(url_for('recetario.consultar_ingredientes_receta', id_rec=id_rec))


@recetario_bp.route('/recetario/editar_ingrediente_receta/<int:id_rec>/<int:id_ing>')
def editar_ingrediente_receta(id_rec, id_ing):
  pass

@recetario_bp.route('/recetario/eliminar_ingrediente_receta/<int:id_rec>/<int:id_ing>')
def eliminar_ingrediente_receta(id_rec, id_ing):
  pass

