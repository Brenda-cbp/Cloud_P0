from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud, auth
from schemas import Usuario, UsuarioCreate, UsuarioIniciarSesion
from database import get_db
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/usuarios", response_model=Usuario)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario_by_nombre_usuario(db, nombre_usuario=usuario.nombre_usuario)
    if db_usuario:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    if not usuario.imagen_perfil:
        usuario.imagen_perfil = "imagen_por_defecto.jpg" 
    usuario.contrasenia= auth.hashear_contrasenia(usuario.contrasenia)
    return crud.crear_usuario(db=db, usuario=usuario)

@router.post("/usuarios/iniciar-sesion", response_model=str)
def iniciar_sesion(usuario: UsuarioIniciarSesion, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario_by_nombre_usuario(db, nombre_usuario=usuario.nombre_usuario)
    if not db_usuario or not auth.verificar_contrasenia(usuario.contrasenia, db_usuario.contrasenia):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = auth.crear_token_acceso(data={"sub": db_usuario.nombre_usuario})
    return JSONResponse(content={"access_token": token, "token_type": "bearer", "user_id": db_usuario.id, "nombre_usuario": db_usuario.nombre_usuario, "imagen_perfil": db_usuario.imagen_perfil})