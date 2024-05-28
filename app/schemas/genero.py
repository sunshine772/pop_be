from pydantic import BaseModel

class GeneroBase(BaseModel):
    nombre: str
    estado: bool = False

class GeneroCreate(GeneroBase):
    pass

class Genero(GeneroBase):
    genero_id: int

    class Config:
        orm_mode = True
