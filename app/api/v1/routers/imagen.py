from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Response
from sqlalchemy.orm import Session
from app.schemas.imagen import Imagen, ImagenCreate
from app.crud.imagen import create_imagen, get_imagen, get_imagenes, update_imagen, delete_imagen
from app.dependencies import get_db, get_current_usuario

router = APIRouter(
    prefix="/api/v1/imagenes",
    tags=["imagenes"]
)

@router.post("/", response_model=int)
def create_image(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: Imagen = Depends(get_current_usuario)):
    file_data = file.file.read()
    imagen = ImagenCreate(
        nombre=file.filename,
        tipo=file.content_type,
        tamaño=len(file_data),
        estado=True,
        imagen=file_data
    )
    created_image = create_imagen(db=db, imagen=imagen)
    return created_image.imagen_id

@router.get("/", response_model=list[Imagen])
def read_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Imagen = Depends(get_current_usuario)):
    images = get_imagenes(db, skip=skip, limit=limit)
    return images

@router.get("/{image_id}", response_class=Response)
def read_image(image_id: int, db: Session = Depends(get_db), current_user: Imagen = Depends(get_current_usuario)):
    db_image = get_imagen(db, imagen_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")
    return Response(content=db_image.imagen, media_type=db_image.tipo)

@router.put("/{image_id}", response_model=Imagen)
def update_image(image_id: int, file: UploadFile = File(...), db: Session = Depends(get_db), current_user: Imagen = Depends(get_current_usuario)):
    file_data = file.file.read()
    imagen = ImagenCreate(
        nombre=file.filename,
        tipo=file.content_type,
        tamaño=len(file_data),
        estado=True,
        imagen=file_data
    )
    return update_imagen(db=db, imagen_id=image_id, imagen=imagen)

@router.delete("/{image_id}", response_model=Imagen)
def delete_image(image_id: int, db: Session = Depends(get_db), current_user: Imagen = Depends(get_current_usuario)):
    db_image = get_imagen(db, imagen_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")
    return delete_imagen(db=db, imagen_id=image_id)
