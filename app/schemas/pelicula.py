from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PeliculaBase(BaseModel):
    ruta: str
    titulo: str
    sinopsis: str
    fecha_estreno: datetime
    estado: bool = False

class PeliculaCreate(PeliculaBase):
    imagen_id: int
    genero_id: int

class Pelicula(PeliculaBase):
    pelicula_id: int

    class Config:
        orm_mode = True
