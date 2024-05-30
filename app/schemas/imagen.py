from pydantic import BaseModel
from typing import Optional

class ImagenBase(BaseModel):
    nombre: str
    tipo: str
    tamaño: int
    estado: bool

class ImagenCreate(ImagenBase):
    imagen: bytes

class Imagen(ImagenBase):
    imagen_id: int
    imagen: Optional[str] = None

    class Config:
        orm_mode = True
