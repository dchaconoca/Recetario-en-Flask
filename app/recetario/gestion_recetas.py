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

def lista_dinamica_recetas(id_cat=-1, id_ing=-1):
  sql = "SELECT R.id, R.titulo "\
        "FROM Receta R "

  if id_ing != -1:
    sql = sql + "INNER JOIN IngredienteReceta IR "\
                "ON R.id = IR.receta_id "\
                "WHERE IR.ingrediente_id = " + str(id_ing)
    if id_cat != -1:
      sql = sql + " AND R.categoria_id = " + str(id_cat)

    sql = sql + " ORDER BY R.titulo"    
      
    return db.session.execute(sql).fetchall()
  
  elif id_cat != -1:
    # sql = sql + "WHERE R.categoria_id = " + str(id_cat)
    # sql = sql + " ORDER BY R.titulo"    
      
    return Receta.recetas_categoria(id_cat)
  
  else:
    return Receta.listar()
