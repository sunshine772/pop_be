from sqlalchemy import Column, String, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.connection import Base

class Token(Base):
    __tablename__ = "tokens"

    access_token = Column(String(450), primary_key=True, index=True)
    refresh_token = Column(String(450), nullable=False)
    estado = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey("usuarios.usuario_id"), nullable=False)
    
    usuario = relationship("Usuario")
