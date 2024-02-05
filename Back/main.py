from typing import Union

from fastapi import FastAPI
from databases import Database
from database import engine
from models import Base
from routes import categorias, tareas, usuarios
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:3000"   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
# Crear todas las tablas definidas en los modelos
Base.metadata.create_all(bind=engine)
app.include_router(categorias.router)
app.include_router(tareas.router)
app.include_router(usuarios.router)
