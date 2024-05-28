from sqlalchemy.orm import Session
from app.models.pelicula import Pelicula
from app.schemas.pelicula import PeliculaCreate

def create_pelicula(db: Session, pelicula: PeliculaCreate):
    db_pelicula = Pelicula(
        ruta=pelicula.ruta,
        titulo=pelicula.titulo,
        sinopsis=pelicula.sinopsis,
        fecha_estreno=pelicula.fecha_estreno,
        estado=pelicula.estado,
        imagen_id=pelicula.imagen_id,
        genero_id=pelicula.genero_id
    )
    db.add(db_pelicula)
    db.commit()
    db.refresh(db_pelicula)
    return db_pelicula

def get_pelicula(db: Session, pelicula_id: int):
    return db.query(Pelicula).filter(Pelicula.pelicula_id == pelicula_id).first()

def get_peliculas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Pelicula).offset(skip).limit(limit).all()

def update_pelicula(db: Session, pelicula_id: int, pelicula: PeliculaCreate):
    db_pelicula = db.query(Pelicula).filter(Pelicula.pelicula_id == pelicula_id).first()
    if db_pelicula:
        db_pelicula.ruta = pelicula.ruta
        db_pelicula.titulo = pelicula.titulo
        db_pelicula.sinopsis = pelicula.sinopsis
        db_pelicula.fecha_estreno = pelicula.fecha_estreno
        db_pelicula.estado = pelicula.estado
        db_pelicula.imagen_id = pelicula.imagen_id
        db_pelicula.genero_id = pelicula.genero_id
        db.commit()
        db.refresh(db_pelicula)
    return db_pelicula

def delete_pelicula(db: Session, pelicula_id: int):
    db_pelicula = db.query(Pelicula).filter(Pelicula.pelicula_id == pelicula_id).first()
    if db_pelicula:
        db.delete(db_pelicula)
        db.commit()
    return db_pelicula
