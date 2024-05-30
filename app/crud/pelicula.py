from sqlalchemy.orm import Session
from app.models.pelicula import Pelicula
from app.schemas.pelicula import PeliculaCreate
import base64


def create_pelicula(db: Session, pelicula: PeliculaCreate):
    db_pelicula = Pelicula(
        titulo=pelicula.titulo,
        sinopsis=pelicula.sinopsis,
        fecha_estreno=pelicula.fecha_estreno,
        estado=pelicula.estado,
        imagen_id=pelicula.imagen_id,
        genero_id=pelicula.genero_id,
    )
    db.add(db_pelicula)
    db.commit()
    db.refresh(db_pelicula)
    return db_pelicula


def get_pelicula(db: Session, pelicula_id: int):
    return db.query(Pelicula).filter(Pelicula.pelicula_id == pelicula_id).first()


def get_peliculas(db: Session, skip: int = 0, limit: int = 10):
    peliculas = db.query(Pelicula).offset(skip).limit(limit).all()
    for pelicula in peliculas:
        if pelicula.imagen and isinstance(pelicula.imagen.imagen, bytes):
            pelicula.imagen.imagen = base64.b64encode(pelicula.imagen.imagen).decode(
                "utf-8"
            )
    return peliculas


def update_pelicula(db: Session, pelicula_id: int, pelicula: PeliculaCreate):
    db_pelicula = db.query(Pelicula).filter(Pelicula.pelicula_id == pelicula_id).first()
    if db_pelicula:
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
