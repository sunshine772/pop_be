from pydantic import BaseModel

class PeliculaEtiquetaBase(BaseModel):
    pelicula_id: int
    etiqueta_id: int

class PeliculaEtiquetaCreate(PeliculaEtiquetaBase):
    pass

class PeliculaEtiqueta(PeliculaEtiquetaBase):
    class Config:
        orm_mode = True
