from fastapi import APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from schemas import CategoriaCreate, Categoria
from crud import create_category, delete_category, get_categories, get_categories_by_name
from fastapi import Depends
from auth import verify_token

router = APIRouter()

@router.post("/categorias", response_model=Categoria)
def create_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    db_categoria = get_categories_by_name(db, name=categoria.nombre)
    if db_categoria:
        raise HTTPException(status_code=400, detail="Ya existe una categoría con este nombre")
    return create_category(db, categoria)

@router.delete("/categorias/{categoria_id}")
def delete_categoria(categoria_id: int, db: Session = Depends(get_db),token: str = Depends(verify_token)):
    return delete_category(db, categoria_id)

@router.get("/categorias", response_model=List[Categoria])
def get_categorias(db: Session = Depends(get_db),token: str = Depends(verify_token)):
    return get_categories(db)