from pydantic import BaseModel

class ImagenBase(BaseModel):
    ruta: str
    nombre: str
    tipo: str
    tamaño: int
    estado: bool

class ImagenCreate(ImagenBase):
    pass

class Imagen(ImagenBase):
    imagen_id: int

    class Config:
        orm_mode = True
