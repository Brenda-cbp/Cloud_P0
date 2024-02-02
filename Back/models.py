#Creación de la BD

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as UserEnum

Base = declarative_base()

class EstadoTarea(UserEnum):
    SIN_EMPEZAR = "Sin Empezar"
    EMPEZADA = "Empezada"
    FINALIZADA = "Finalizada"

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String)
    contrasenia = Column(String)
    imagen_perfil = Column(String)
    tareas = relationship("Tarea", back_populates="usuario")

class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(String)
    tareas = relationship("Tarea", back_populates="categoria")

class Tarea(Base):
    __tablename__ = 'tareas'

    id = Column(Integer, primary_key=True, index=True)
    texto_tarea = Column(String)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_tentativa_finalizacion = Column(DateTime)
    estado = Column(Enum(EstadoTarea))
    id_categoria = Column(Integer, ForeignKey('categorias.id'))
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))

    categoria = relationship("Categoria", back_populates="tareas")
    usuario = relationship("Usuario", back_populates="tareas")
