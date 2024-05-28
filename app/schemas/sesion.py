from pydantic import BaseModel
from typing import Optional

class SesionBase(BaseModel):
    token_sesion: str
    estado: bool = False

class SesionCreate(SesionBase):
    usuario_id: int
    username: str
    password: str
    
class Sesion(SesionBase):
    sesion_id: int

    class Config:
        orm_mode = True
