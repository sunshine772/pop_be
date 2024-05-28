from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    username: str
    email: str
    estado: bool = True
    is_admin: bool = False

class UsuarioCreate(UsuarioBase):
    password: str

class request_details(BaseModel):
    email:str
    password:str

class Usuario(UsuarioBase):
    usuario_id: int

    class Config:
        orm_mode = True
