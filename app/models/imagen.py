from sqlalchemy import Column, String, Boolean, Integer, LargeBinary
from app.database.connection import Base

class Imagen(Base):
    __tablename__ = "imagenes"

    imagen_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    tamaño = Column(Integer, nullable=False)
    estado = Column(Boolean, default=True)
    imagen = Column(LargeBinary, nullable=False)
