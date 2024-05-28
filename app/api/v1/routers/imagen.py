from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.imagen import Imagen, ImagenCreate
from app.crud.imagen import create_imagen, get_imagen, get_imagenes, update_imagen, delete_imagen
from app.dependencies import get_db, get_current_usuario

router = APIRouter(
    prefix="/api/v1/imagenes",
    tags=["imagenes"]
)

@router.post("/", response_model=Imagen)
def create_image(image: ImagenCreate, db: Session = Depends(get_db)):
    return create_imagen(db=db, imagen=image)

@router.get("/", response_model=list[Imagen])
def read_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Imagen = Depends(get_current_usuario)):
    images = get_imagenes(db, skip=skip, limit=limit)
    return images

@router.get("/{image_id}", response_model=Imagen)
def read_image(image_id: int, db: Session = Depends(get_db), current_user: Imagen = Depends(get_current_usuario)):
    db_image = get_imagen(db, imagen_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")
    return db_image

@router.put("/{image_id}", response_model=Imagen)
def update_image(image_id: int, image: ImagenCreate, db: Session = Depends(get_db), current_user: Imagen = Depends(get_current_usuario)):
    db_image = get_imagen(db, imagen_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")
    return update_imagen(db=db, imagen_id=image_id, imagen=image)

@router.delete("/{image_id}", response_model=Imagen)
def delete_image(image_id: int, db: Session = Depends(get_db), current_user: Imagen = Depends(get_current_usuario)):
    db_image = get_imagen(db, imagen_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")
    return delete_imagen(db=db, imagen_id=image_id)
