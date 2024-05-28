from sqlalchemy.orm import Session
from app.models.sesion import Sesion
from app.schemas.sesion import SesionCreate

def create_sesion(db: Session, sesion: SesionCreate):
    db_sesion = Sesion(
        token_sesion=sesion.token_sesion,
        estado=sesion.estado,
        usuario_id=sesion.usuario_id
    )
    db.add(db_sesion)
    db.commit()
    db.refresh(db_sesion)
    return db_sesion

def get_sesion(db: Session, sesion_id: int):
    return db.query(Sesion).filter(Sesion.sesion_id == sesion_id).first()

def get_sesiones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Sesion).offset(skip).limit(limit).all()

def update_sesion(db: Session, sesion_id: int, sesion: SesionCreate):
    db_sesion = db.query(Sesion).filter(Sesion.sesion_id == sesion_id).first()
    if db_sesion:
        db_sesion.token_sesion = sesion.token_sesion
        db_sesion.estado = sesion.estado
        db_sesion.usuario_id = sesion.usuario_id
        db.commit()
        db.refresh(db_sesion)
    return db_sesion

def delete_sesion(db: Session, sesion_id: int):
    db_sesion = db.query(Sesion).filter(Sesion.sesion_id == sesion_id).first()
    if db_sesion:
        db.delete(db_sesion)
        db.commit()
    return db_sesion
