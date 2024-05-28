from pydantic import BaseModel

class ComentarioBase(BaseModel):
    comentario: str
    estado: bool = True

class ComentarioCreate(ComentarioBase):
    usuario_id: int
    pelicula_id: int

class Comentario(ComentarioBase):
    comentario_id: int

    class Config:
        orm_mode = True
