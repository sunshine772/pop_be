from pydantic import BaseModel

class EtiquetaBase(BaseModel):
    nombre: str
    estado: bool = False

class EtiquetaCreate(EtiquetaBase):
    pass

class Etiqueta(EtiquetaBase):
    etiqueta_id: int

    class Config:
        orm_mode = True
