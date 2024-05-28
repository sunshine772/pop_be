from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database.connection import Base

class Sesion(Base):
    __tablename__ = 'sesiones'

    sesion_id = Column(Integer, primary_key=True, index=True)
    token_sesion = Column(String(255), unique=True)
    estado = Column(Boolean, default=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.usuario_id', ondelete='RESTRICT', onupdate='RESTRICT'))
