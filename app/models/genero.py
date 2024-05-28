from sqlalchemy import Column, Integer, String, Boolean
from app.database.connection import Base

class Genero(Base):
    __tablename__ = 'generos'

    genero_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    estado = Column(Boolean, default=False)
