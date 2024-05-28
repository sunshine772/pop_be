from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, TIMESTAMP
from app.database.connection import Base

class Pelicula(Base):
    __tablename__ = 'peliculas'

    pelicula_id = Column(Integer, primary_key=True, index=True)
    ruta = Column(String(255))
    titulo = Column(String(50))
    sinopsis = Column(Text)
    fecha_estreno = Column(TIMESTAMP)
    estado = Column(Boolean, default=False)
    imagen_id = Column(Integer, ForeignKey('imagenes.imagen_id', ondelete='RESTRICT', onupdate='RESTRICT'))
    genero_id = Column(Integer, ForeignKey('generos.genero_id', ondelete='RESTRICT', onupdate='RESTRICT'))
