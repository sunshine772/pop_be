from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database.connection import Base

class Comentario(Base):
    __tablename__ = 'comentarios'

    comentario_id = Column(Integer, primary_key=True, index=True)
    comentario = Column(String(200))
    estado = Column(Boolean, default=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.usuario_id', ondelete='RESTRICT', onupdate='RESTRICT'))
    pelicula_id = Column(Integer, ForeignKey('peliculas.pelicula_id', ondelete='RESTRICT', onupdate='RESTRICT'))
