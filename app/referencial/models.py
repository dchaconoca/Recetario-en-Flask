#########################################################
# MODELOS DEL REFERENCIAL
# Aquí se definen todas las tablas que sirven 
# de referencial
#########################################################

# SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import Column, Integer, String
from sqlalchemy import Float
from sqlalchemy.orm import backref
from sqlalchemy.sql.expression import true

# Base de datos
from app import db

# Tabla de Categorias de recetas
class Categoria(db.Model):

    __tablename__='Categoria'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(100))

    # Devuelve el nombre
    def __str__(self):
        return self.nombre

    # Hace las diversas validaciones de la categoria
    def validar(self):
        valido = False
        if self.nombre != None and len(self.nombre) <= 50 and len(self.descripcion) <= 100:
            valido = true
        return valido

    # Guarda una categoria, ya sea nueva o existente (id)
    def guardar(self):
        if not self.id:
            db.session.add(self)
        else:
            categoria = {'nombre': self.nombre, 'descripcion': self.descripcion}
            self.query.filter_by(id=self.id).update(categoria)
        db.session.commit()

    # Elimina una categoria dada (id)
    def borrar(self, id):
        borrado = self.query.filter_by(id=id).delete()
        db.session.commit()

        return borrado

    # Devuelve una categoria dada (id)
    def buscar(self, id):
        return self.query.get(id)

    # Devuelve la lista de todas las categorias
    def listar(self):
        return self.query.order_by(Categoria.nombre).all()

# Tabla de Unidades de Medida
# Utilizada en los ingredientes para especificar el precio según su unidad de medida
# Y en la lista de ingredientes de una receta
class Medida(db.Model):

    __tablename__='Medida'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    proporcion = Column(Float, default=1, nullable=False) 

    # Devuelve el nombre
    def __str__(self):
        return self.nombre

    # Hace las diversas validaciones de la unidad de medida
    def validar(self):
        valido = False
        if self.nombre != None and len(self.nombre) <= 50 and self.proporcion != None:
            valido = True
        return valido

    # Guarda una medida, ya sea nueva o existente (id)
    def guardar(self):
        if not self.id:
            db.session.add(self)
        else:
            medida = {'nombre': self.nombre, 'proporcion': self.proporcion}
            self.query.filter_by(id=self.id).update(medida)
        db.session.commit()

    # Elimina una categoria dada (id)
    def borrar(self, id):
        borrado = self.query.filter_by(id=id).delete()
        db.session.commit()

        return borrado

    # Devuelve una categoria dada (id)
    def buscar(self, id):
        return self.query.get(id)

    # Devuelve la lista de todas las categorias
    def listar(self):
        return self.query.order_by(Medida.nombre).all()


