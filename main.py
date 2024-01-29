from typing import Union

from fastapi import FastAPI
from databases import Database
from database import engine
from models import Base
from routes import categorias, tareas, usuarios

app = FastAPI()

# Crear todas las tablas definidas en los modelos
Base.metadata.create_all(bind=engine)
app.include_router(categorias.router)
app.include_router(tareas.router)
app.include_router(usuarios.router)
