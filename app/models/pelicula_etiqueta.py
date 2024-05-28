from sqlalchemy import Column, Integer, ForeignKey
from app.database.connection import Base

class PeliculaEtiqueta(Base):
    __tablename__ = 'peliculas_etiquetas'

    pelicula_id = Column(Integer, ForeignKey('peliculas.pelicula_id', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True)
    etiqueta_id = Column(Integer, ForeignKey('etiquetas.etiqueta_id', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True)
