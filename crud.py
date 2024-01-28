#Lógica para los requerimientos
from sqlalchemy.orm import Session
from models import Categoria, Tarea
from schemas import CategoriaCreate, TareaCreate, TareaUpdate
from fastapi import APIRouter, HTTPException

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
    db.delete(db_categoria)
    db.commit()
    return {"message": "Categoría eliminada"}

def get_categories(db: Session):
    return db.query(Categoria).all()

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

def get_task(db: Session):
    return db.query(Tarea).all()
