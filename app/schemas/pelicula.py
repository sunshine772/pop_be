from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.schemas.genero import Genero
from app.schemas.imagen import Imagen

class PeliculaBase(BaseModel):
    titulo: str
    sinopsis: str
    fecha_estreno: datetime
    estado: bool = False


class Pelicula(PeliculaBase):
    pelicula_id: int
    imagen: Optional[Imagen]
    genero: Optional[Genero]

    class Config:
        orm_mode = True


class PeliculaCreate(PeliculaBase):
    imagen_id: int
    genero_id: int
