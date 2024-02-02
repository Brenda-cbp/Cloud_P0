from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
import jwt
from jose import JWTError
from passlib.context import CryptContext
from typing import Optional
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

bearer_scheme = HTTPBearer()

SECRET_KEY = "n4ruljhfflef9494q@lS4WqFZbmD9B9l"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_contrasenia(contrasenia_plana, contrasenia_hasheada):
    return crypt_context.verify(contrasenia_plana, contrasenia_hasheada)

def hashear_contrasenia(contrasenia):
    return crypt_context.hash(contrasenia)

def crear_token_acceso(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def extract_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> str:
    if credentials is None or "bearer" not in credentials.scheme.lower():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Esquema de autenticación no válido. Se esperaba 'Bearer'",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials

def verify_token(token: str = Depends(extract_token)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pueden validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception
