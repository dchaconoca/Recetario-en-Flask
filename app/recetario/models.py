#########################################################
# MODELOS DE RECETAS
# Aquí se definen todas las tablas que sirven 
# para guardar las recetas: Recetas, Ingredientes y
# su relación
#########################################################

# SQLAlchemy
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import DateTime, Float
from sqlalchemy.orm import relationship, backref

# Librerías Python
from datetime import datetime

from sqlalchemy.sql.expression import false, true

# Base de datos
from app import db

# Tablas del referencial
# from app.referencial.models import Categoria, Medida


# Tabla de ingredientes
class Ingrediente(db.Model):

  __tablename__='Ingrediente'
  id = Column(Integer, primary_key=True)
  nombre = Column(String(50), nullable=False)
  descripcion = Column(String(100), nullable=True)
  precio = Column(Float, default=0, nullable=True) 
  medida_id = Column(Integer, ForeignKey('Medida.id', ondelete="CASCADE"), nullable=False)
  medida=relationship("Medida")
  created = Column(DateTime)
  updated = Column(DateTime)

  # Relación
  recetas = relationship("IngredienteReceta", backref="Receta")

  # Devuelve el nombre
  def __str__(self):
      return self.nombre

  # Hace las diversas validaciones del ingrediente
  def validar(self):
      valido = False
      if not self.nombre is None and not self.medida_id is None:
          valido = True
      return valido

  # Guarda un ingrediente, ya sea nuevo o existente (id)
  def guardar(self):
    if not self.id:
      self.created=datetime.now()
      self.updated=datetime.now()
      db.session.add(self)
    else:
      ingrediente = {'nombre': self.nombre, 
                    'descripcion': self.descripcion,
                    'precio': self.precio,
                    'medida_id': self.medida_id,
                    'updated': datetime.now()
                    }
      self.query.filter_by(id=self.id).update(ingrediente)
    db.session.commit()

  # Elimina un ingrediente dado (id)
  def borrar(self, id):
    borrado = self.query.filter_by(id=id).delete()
    db.session.commit()

    return borrado

  # Devuelve un ingrediente dado (id)
  def buscar(self, id):
    return self.query.get(id)

  # Devuelve la lista de todos los ingredientes
  @staticmethod
  def listar():
    return Ingrediente.query.order_by(Ingrediente.nombre).all()


# Tabla de Recetas
class Receta(db.Model):

  __tablename__='Receta'
  id = Column(Integer, primary_key=True)
  titulo = Column(String(50), nullable=False)
  descripcion = Column(Text, nullable=True)
  categoria_id = Column(Integer, ForeignKey('Categoria.id', ondelete="CASCADE"), nullable=False)
  categoria=relationship("Categoria", backref="Receta")
  precio_venta = Column(Float, default=0, nullable=True) 
  created = Column(DateTime)
  updated = Column(DateTime)

  # Relación
  ingredientes_receta = relationship("IngredienteReceta", backref="Ingrediente")

  # Devuelve el nombre
  def __str__(self):
    return self.titulo

  # Hace las diversas validaciones de la receta
  def validar(self):
    valido = False
    if self.titulo != None and self.categoria_id != None:
      valido = True
    return valido

  # Guarda una receta, ya sea nueva o existente (id)
  def guardar(self):
    if not self.id:
      self.created=datetime.now()
      self.updated=datetime.now()
      db.session.add(self)
    else:
      receta =  {'titulo': self.titulo, 
                'descripcion': self.descripcion,
                'precio_venta': self.precio_venta,
                'categoria_id': self.categoria_id,
                'updated': datetime.now()
                }
      self.query.filter_by(id=self.id).update(receta)
    db.session.commit()

  # Elimina una receta dada (id)
  def borrar(self, id):
    borrado = self.query.filter_by(id=id).delete()
    db.session.commit()

    return borrado

  # Devuelve una receta dada (id)
  def buscar(self, id):
    return self.query.get(id)

  
  def buscar_ingredientes(self):
    sql = "SELECT IR.receta_id rec_id, I.id ing_id, I.nombre nombre_ing, "\
          "IR.cantidad cantidad, IR.medida_id med_id, M.nombre nombre_med "\
          "FROM Ingrediente I "\
          "INNER JOIN IngredienteReceta IR "\
          "ON I.id = IR.ingrediente_id "\
          "INNER JOIN Medida M "\
          "ON IR.medida_id= M.id "\
          "WHERE IR.receta_id  = " + str(self.id)    
        
    return db.session.execute(sql).fetchall()
  
  # Busca y eleimina un ingrediente de una receta
  def borrar_ingrediente(self, id_rec, id_ing):
    print("buscar")
    receta = self.buscar(id_rec)
    i = 0
    borrado = false

    for ingrediente in receta.ingredientes_receta:
      print("antes if")
      if ingrediente.ingrediente_id==id_ing:
        print(receta.ingredientes_receta[i])
        borrado = receta.ingredientes_receta.pop(i)
        db.session.commit()
        print(receta.ingredientes_receta)
        print(borrado)
        return borrado

      i=i+1

    return borrado

  # Devuelve la lista de todas las recetas
  @staticmethod
  def listar():
    return Receta.query.order_by(Receta.titulo).all()

  # Devuelve la lista de todas las recetas de una categoria
  @staticmethod
  def recetas_categoria(cat_id):
    return Receta.query.filter_by(categoria_id=cat_id).order_by(Receta.titulo).all()


# Tabla de IngredienteReceta
# Asocia recetas con ingredientes
# Relación many to many bidireccional, o sea, permite obtener la lista de
# ingredientes de una receta pero también la lista de recetas que contienen
# un ingediente
class IngredienteReceta(db.Model):

  __tablename__='IngredienteReceta'
  receta_id = Column(Integer, ForeignKey('Receta.id', ondelete="CASCADE"), primary_key=True)
  ingrediente_id = Column(Integer, ForeignKey('Ingrediente.id', ondelete="CASCADE"), primary_key=True) 
  cantidad = Column(Float, default=1, nullable=False) 
  medida_id = Column(Integer, ForeignKey('Medida.id', ondelete="CASCADE"), nullable=False)
  medida=relationship("Medida")
  created = Column(DateTime)
  updated = Column(DateTime)
  
  # Relaciones
  receta = relationship("Receta",  cascade="all,delete", backref="recetas")
  ingrediente = relationship("Ingrediente",  cascade="all,delete", backref="ingredientes")

  # Hace las diversas validaciones para los ingredientes de una receta
  def validar(self):
    valido = False
    if self.ingrediente_id != None and self.cantidad != None and self.medida_id !=  None:
      valido = True
    return valido

  # Guarda ingredientes de una receta
  def guardar(self):

    existe = IngredienteReceta.query.filter_by(receta_id=self.receta_id, ingrediente_id=self.ingrediente_id)

    if not existe:
      self.created=datetime.now()
      self.updated=datetime.now()
      db.session.add(self)
    else:
      ing_receta =  {'receta_id': self.receta_id, 
                'ingrediente_id': self.ingrediente_id,
                'cantidad': self.cantidad,
                'medida_id': self.medida_id,
                'updated': datetime.now()
                }
      self.query.filter_by(receta_id=self.receta_id, ingrediente_id=self.ingrediente_id).update(ing_receta)
    db.session.commit()

  # Elimina un ingrediente de una receta
  def borrar(self, id_rec, id_ing):

    una_receta = Receta()
    receta = una_receta.buscar(id_rec)
    print("Borrando")
    borrado = self.query.filter_by(receta_id=id_rec, ingrediente_id=id_ing).all()
    print(borrado)
    # db.session.commit()
    print(borrado)
    return borrado
