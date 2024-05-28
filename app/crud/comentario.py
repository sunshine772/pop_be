from sqlalchemy.orm import Session
from app.models.comentario import Comentario
from app.schemas.comentario import ComentarioCreate

def create_comentario(db: Session, comentario: ComentarioCreate):
    db_comentario = Comentario(
        comentario=comentario.comentario,
        estado=comentario.estado,
        usuario_id=comentario.usuario_id,
        pelicula_id=comentario.pelicula_id
    )
    db.add(db_comentario)
    db.commit()
    db.refresh(db_comentario)
    return db_comentario

def get_comentario(db: Session, comentario_id: int):
    return db.query(Comentario).filter(Comentario.comentario_id == comentario_id).first()

def get_comentarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Comentario).offset(skip).limit(limit).all()

def update_comentario(db: Session, comentario_id: int, comentario: ComentarioCreate):
    db_comentario = db.query(Comentario).filter(Comentario.comentario_id == comentario_id).first()
    if db_comentario:
        db_comentario.comentario = comentario.comentario
        db_comentario.estado = comentario.estado
        db_comentario.usuario_id = comentario.usuario_id
        db_comentario.pelicula_id = comentario.pelicula_id
        db.commit()
        db.refresh(db_comentario)
    return db_comentario

def delete_comentario(db: Session, comentario_id: int):
    db_comentario = db.query(Comentario).filter(Comentario.comentario_id == comentario_id).first()
    if db_comentario:
        db.delete(db_comentario)
        db.commit()
    return db_comentario
