from sqlalchemy.orm import Session
from app.models.etiqueta import Etiqueta
from app.schemas.etiqueta import EtiquetaCreate

def create_etiqueta(db: Session, etiqueta: EtiquetaCreate):
    db_etiqueta = Etiqueta(
        nombre=etiqueta.nombre,
        estado=etiqueta.estado
    )
    db.add(db_etiqueta)
    db.commit()
    db.refresh(db_etiqueta)
    return db_etiqueta

def get_etiqueta(db: Session, etiqueta_id: int):
    return db.query(Etiqueta).filter(Etiqueta.etiqueta_id == etiqueta_id).first()

def get_etiquetas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Etiqueta).offset(skip).limit(limit).all()

def update_etiqueta(db: Session, etiqueta_id: int, etiqueta: EtiquetaCreate):
    db_etiqueta = db.query(Etiqueta).filter(Etiqueta.etiqueta_id == etiqueta_id).first()
    if db_etiqueta:
        db_etiqueta.nombre = etiqueta.nombre
        db_etiqueta.estado = etiqueta.estado
        db.commit()
        db.refresh(db_etiqueta)
    return db_etiqueta

def delete_etiqueta(db: Session, etiqueta_id: int):
    db_etiqueta = db.query(Etiqueta).filter(Etiqueta.etiqueta_id == etiqueta_id).first()
    if db_etiqueta:
        db.delete(db_etiqueta)
        db.commit()
    return db_etiqueta
