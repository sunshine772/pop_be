from sqlalchemy import Column, Integer, String, Boolean
from app.database.connection import Base

class Etiqueta(Base):
    __tablename__ = 'etiquetas'

    etiqueta_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    estado = Column(Boolean, default=False)
