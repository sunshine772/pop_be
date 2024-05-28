from sqlalchemy import Column, Integer, String, Boolean
from app.database.connection import Base

class Imagen(Base):
    __tablename__ = 'imagenes'

    imagen_id = Column(Integer, primary_key=True, index=True)
    ruta = Column(String(255))
    nombre = Column(String(255))
    tipo = Column(String(50))
    tamaño = Column(Integer)
    estado = Column(Boolean, default=True)
