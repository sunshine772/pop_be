from pydantic import BaseModel

class ImagenBase(BaseModel):
    nombre: str
    tipo: str
    tamaño: int
    estado: bool

class ImagenCreate(ImagenBase):
    imagen: bytes
    
class Imagen(ImagenBase):
    imagen_id: int

    class Config:
        orm_mode = True
