#########################################################
# GESTIÓN DE RECETAS
# Módulo donde se definen todas las reglas de negocio
# para la gestión de las recetas, sus ingredientes y
# el cálculo de sus costos y precios
# De esta manera, models.py se encarga de definir los
# modelos y la comunicación con la base de datos
# y routes.py se encarga únicamente de llamar el 
# presente módulo y gestionar la comunicación con 
# el front
#########################################################

from .models import Ingrediente, Receta, IngredienteReceta
from app.referencial.models import Medida, Categoria
from app import db

# Devuelve una lista de recetas para una categoría y/o
# ingrediente
def lista_dinamica_recetas(id_cat=None, id_ing=None):
  sql = "SELECT R.id, R.titulo "\
        'FROM "Receta" R '

  if id_ing:
    sql = sql + 'INNER JOIN "IngredienteReceta" IR '\
                "ON R.id = IR.receta_id "\
                "WHERE IR.ingrediente_id = " + str(id_ing)
    if id_cat:
      sql = sql + " AND R.categoria_id = " + str(id_cat)

    sql = sql + " ORDER BY R.titulo"    
      
    return db.session.execute(sql).fetchall()
  
  elif id_cat:      
    return Receta.recetas_categoria(id_cat)
  
  else:
    return Receta.listar()

# Llama un stored procedure de la base de datos que devuelve el costo 
# de una receta dada
def calculo_costo_receta(id):
  sql = "select fn_costo_receta(" + str(id) + ")"
  
  costo = (db.session.execute(sql).first()[0] if db.session.execute(sql).first() else 0)
  
  return costo


# Calcula el precio en función del costo y la ganacia
def calculo_precio_receta(costo, ganancia):
  precio = 0
  if costo:
    precio = (float(costo) * (1.0 + float(ganancia / 100))) 
  return precio
