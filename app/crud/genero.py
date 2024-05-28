from sqlalchemy.orm import Session
from app.models.genero import Genero
from app.schemas.genero import GeneroCreate

def create_genero(db: Session, genero: GeneroCreate):
    db_genero = Genero(
        nombre=genero.nombre,
        estado=genero.estado
    )
    db.add(db_genero)
    db.commit()
    db.refresh(db_genero)
    return db_genero

def get_genero(db: Session, genero_id: int):
    return db.query(Genero).filter(Genero.genero_id == genero_id).first()

def get_generos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Genero).offset(skip).limit(limit).all()

def update_genero(db: Session, genero_id: int, genero: GeneroCreate):
    db_genero = db.query(Genero).filter(Genero.genero_id == genero_id).first()
    if db_genero:
        db_genero.nombre = genero.nombre
        db_genero.estado = genero.estado
        db.commit()
        db.refresh(db_genero)
    return db_genero

def delete_genero(db: Session, genero_id: int):
    db_genero = db.query(Genero).filter(Genero.genero_id == genero_id).first()
    if db_genero:
        db.delete(db_genero)
        db.commit()
    return db_genero
