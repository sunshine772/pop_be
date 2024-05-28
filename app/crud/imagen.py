from sqlalchemy.orm import Session
from app.models.imagen import Imagen
from app.schemas.imagen import ImagenCreate

def create_imagen(db: Session, imagen: ImagenCreate):
    db_imagen = Imagen(
        ruta=imagen.ruta,
        nombre=imagen.nombre,
        tipo=imagen.tipo,
        tamaño=imagen.tamaño,
        estado=imagen.estado
    )
    db.add(db_imagen)
    db.commit()
    db.refresh(db_imagen)
    return db_imagen

def get_imagen(db: Session, imagen_id: int):
    return db.query(Imagen).filter(Imagen.imagen_id == imagen_id).first()

def get_imagenes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Imagen).offset(skip).limit(limit).all()

def update_imagen(db: Session, imagen_id: int, imagen: ImagenCreate):
    db_imagen = db.query(Imagen).filter(Imagen.imagen_id == imagen_id).first()
    if db_imagen:
        db_imagen.ruta = imagen.ruta
        db_imagen.nombre = imagen.nombre
        db_imagen.tipo = imagen.tipo
        db_imagen.tamaño = imagen.tamaño
        db_imagen.estado = imagen.estado
        db.commit()
        db.refresh(db_imagen)
    return db_imagen

def delete_imagen(db: Session, imagen_id: int):
    db_imagen = db.query(Imagen).filter(Imagen.imagen_id == imagen_id).first()
    if db_imagen:
        db.delete(db_imagen)
        db.commit()
    return db_imagen
