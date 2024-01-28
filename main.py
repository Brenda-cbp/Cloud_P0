from typing import Union

from fastapi import FastAPI
from databases import Database
from database import engine, get_db
from models import Base
from routes import categorias, tareas

app = FastAPI()

# Crear todas las tablas definidas en los modelos
Base.metadata.create_all(bind=engine)
app.include_router(categorias.router)
app.include_router(tareas.router)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/task/{task_id}")
# def read_item(task_id: int, q: Union[str, None] = None):
#     return {"task_id": task_id, "q": q}