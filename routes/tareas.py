from fastapi import APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from schemas import TareaCreate, Tarea, TareaUpdate
from crud import create_task, delete_task, get_task, update_task
from fastapi import Depends

router = APIRouter()

@router.post("/tareas", response_model=Tarea)
def create_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    return create_task(db, tarea)

@router.put("/tareas/{tarea_id}", response_model=Tarea)
def update_tarea(tarea_id: int, tarea: TareaUpdate, db: Session = Depends(get_db)):
    updated_tarea = update_task(db, tarea_id, tarea)
    if updated_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return updated_tarea

@router.delete("/tareas/{tarea_id}")
def delete_tarea(tarea_id: int, db: Session = Depends(get_db)):
    return delete_task(db, tarea_id)

@router.get("/tareas", response_model=List[Tarea])
def get_tarea(db: Session = Depends(get_db)):
    return get_task(db)