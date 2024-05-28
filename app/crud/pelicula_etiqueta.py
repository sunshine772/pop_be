from sqlalchemy.orm import Session
from app.models.pelicula_etiqueta import PeliculaEtiqueta
from app.schemas.pelicula_etiqueta import PeliculaEtiquetaCreate

def create_pelicula_etiqueta(db: Session, pelicula_etiqueta: PeliculaEtiquetaCreate):
    db_pelicula_etiqueta = PeliculaEtiqueta(
        pelicula_id=pelicula_etiqueta.pelicula_id,
        etiqueta_id=pelicula_etiqueta.etiqueta_id
    )
    db.add(db_pelicula_etiqueta)
    db.commit()
    db.refresh(db_pelicula_etiqueta)
    return db_pelicula_etiqueta

def get_pelicula_etiqueta(db: Session, pelicula_id: int, etiqueta_id: int):
    return db.query(PeliculaEtiqueta).filter(
        PeliculaEtiqueta.pelicula_id == pelicula_id,
        PeliculaEtiqueta.etiqueta_id == etiqueta_id
    ).first()

def get_peliculas_etiquetas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PeliculaEtiqueta).offset(skip).limit(limit).all()

def delete_pelicula_etiqueta(db: Session, pelicula_id: int, etiqueta_id: int):
    db_pelicula_etiqueta = db.query(PeliculaEtiqueta).filter(
        PeliculaEtiqueta.pelicula_id == pelicula_id,
        PeliculaEtiqueta.etiqueta_id == etiqueta_id
    ).first()
    if db_pelicula_etiqueta:
        db.delete(db_pelicula_etiqueta)
        db.commit()
    return db_pelicula_etiqueta
