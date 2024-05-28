from sqlalchemy import Column, Integer, String, Boolean
from app.database.connection import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    usuario_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(200))
    email = Column(String(50), unique=True, index=True)
    estado = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
