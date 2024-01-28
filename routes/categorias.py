from fastapi import APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from schemas import CategoriaCreate, Categoria
from crud import create_category, delete_category, get_categories
from fastapi import Depends

router = APIRouter()

@router.post("/categorias", response_model=Categoria)
def create_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return create_category(db, categoria)

@router.delete("/categorias/{categoria_id}")
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    return delete_category(db, categoria_id)

@router.get("/categorias", response_model=List[Categoria])
def get_categorias(db: Session = Depends(get_db)):
    return get_categories(db)