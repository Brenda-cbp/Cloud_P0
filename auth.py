from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext

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

def decodificar_token_acceso(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        return None
