#Incluye las definiciones de los modelos Pydantic para validación de datos en las solicitudes y respuestas.
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
#------------------------------------------------------------------
# C A T E G O R I A S 
#------------------------------------------------------------------
class CategoriaBase(BaseModel):
    nombre: str
    descripcion: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int

    class Config:
        orm_mode = True

#------------------------------------------------------------------
# T A R E A S
#------------------------------------------------------------------

class TareaBase(BaseModel):
    texto_tarea: str
    fecha_creacion: datetime = datetime.now()
    fecha_tentativa_finalizacion: Optional[datetime]
    estado: str
    id_categoria: int
    #id_usuario : int

class TareaCreate(TareaBase):
    pass

class TareaUpdate(BaseModel):
    texto_tarea: Optional[str]
    fecha_tentativa_finalizacion: Optional[datetime]
    estado: Optional[str]
    
class Tarea(TareaBase):
    id: int

    class Config:
        orm_mode = True