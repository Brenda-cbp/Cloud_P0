from fastapi import APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from schemas import TareaCreate, Tarea, TareaUpdate
from crud import create_task, delete_task, update_task, get_task_by_id, get_task_by_usuario
from fastapi import Depends
from auth import verify_token

router = APIRouter()

@router.post("/tareas", response_model=Tarea)
def create_tarea(tarea: TareaCreate, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    if tarea.estado == "SIN_EMPEZAR" or tarea.estado=="EMPEZADA" or tarea.estado=="FINALIZADA" : 
        return create_task(db, tarea)
    else: 
        raise HTTPException(status_code=400, detail="Valores no válidos para el estado de la tarea. Los permitidos son SIN_EMPEZAR, EMPEZADA, FINALIZADA")

@router.put("/tareas/{tarea_id}", response_model=Tarea)
def update_tarea(tarea_id: int, tarea: TareaUpdate, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    if tarea.estado == "SIN_EMPEZAR" or tarea.estado=="EMPEZADA" or tarea.estado=="FINALIZADA" : 
        updated_tarea = update_task(db, tarea_id, tarea)
        if updated_tarea is None:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        return updated_tarea
    else: 
        raise HTTPException(status_code=400, detail="Valores no válidos para el estado de la tarea. Los permitidos son SIN_EMPEZAR, EMPEZADA, FINALIZADA")

@router.delete("/tareas/{tarea_id}")
def delete_tarea(tarea_id: int, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    return delete_task(db, tarea_id)

@router.get("/tareas/usuario/{usuario_id}", response_model=list[Tarea])
def get_tareas_by_usuario(usuario_id: int, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    tareas = get_task_by_usuario(db, usuario_id)
    if not tareas:
        raise HTTPException(status_code=404, detail="No se encontraron tareas para este usuario")
    return tareas

@router.get("/tareas/{tarea_id}", response_model=Tarea)
def get_tarea(tarea_id: int, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    tarea = get_task_by_id(db, tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea