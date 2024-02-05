#Lógica para los requerimientos
from sqlalchemy.orm import Session
from models import Categoria, Tarea, Usuario
from schemas import CategoriaCreate, TareaCreate, TareaUpdate, UsuarioCreate
from fastapi import APIRouter, HTTPException
from typing import List

#------------------------------------------------------------------
# C A T E G O R I A S 
#------------------------------------------------------------------

def create_category(db: Session, categoria: CategoriaCreate):
    db_categoria = Categoria(**categoria.model_dump())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def delete_category(db: Session, categoria_id: int):
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="La categoría no existe")
    
    tareas_asociadas = db.query(Tarea).filter(Tarea.id_categoria == categoria_id).all()
    if tareas_asociadas:
        raise HTTPException(status_code=400, detail="No se puede eliminar la categoría porque tiene tareas asociadas")

    db.delete(db_categoria)
    db.commit()
    return {"message": "Categoría eliminada"}

def get_categories(db: Session):
    return db.query(Categoria).all()

def get_categories_by_name (db: Session, name: str):
    return db.query(Categoria).filter(Categoria.nombre == name).first()


#------------------------------------------------------------------
# T A R E A S
#------------------------------------------------------------------
def create_task(db: Session, tarea: TareaCreate):
    db_tarea = Tarea(**tarea.model_dump())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def update_task(db: Session, tarea_id: int, tarea: TareaUpdate):
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if db_tarea:
        for key, value in tarea.model_dump(exclude_unset=True).items():
            setattr(db_tarea, key, value)
        db.commit()
        db.refresh(db_tarea)
        return db_tarea
    return None

def delete_task(db: Session, tarea_id: int):
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="La tarea no existe")
    db.delete(db_tarea)
    db.commit()
    return {"message": "Tarea eliminada"}

def get_task_by_usuario(db: Session, usuario_id: int) -> List[Tarea]:
    return db.query(Tarea).filter(Tarea.id_usuario == usuario_id).all()

def get_task_by_id(db: Session, tarea_id: int) -> Tarea:
    return db.query(Tarea).filter(Tarea.id == tarea_id).first()

#------------------------------------------------------------------
# U S U A R I O 
#------------------------------------------------------------------

def get_usuario_by_nombre_usuario(db: Session, nombre_usuario: str):
    return db.query(Usuario).filter(Usuario.nombre_usuario == nombre_usuario).first()

def crear_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(nombre_usuario=usuario.nombre_usuario, contrasenia=usuario.contrasenia, imagen_perfil=usuario.imagen_perfil)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario