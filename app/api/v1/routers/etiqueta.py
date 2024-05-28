from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.etiqueta import Etiqueta, EtiquetaCreate
from app.crud.etiqueta import create_etiqueta, get_etiqueta, get_etiquetas, update_etiqueta, delete_etiqueta
from app.dependencies import get_db, get_current_usuario

router = APIRouter(
    prefix="/api/v1/etiquetas",
    tags=["etiquetas"]
)

@router.post("/", response_model=Etiqueta)
def create_tag(tag: EtiquetaCreate, db: Session = Depends(get_db)):
    return create_etiqueta(db=db, etiqueta=tag)

@router.get("/", response_model=list[Etiqueta])
def read_tags(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Etiqueta = Depends(get_current_usuario)):
    tags = get_etiquetas(db, skip=skip, limit=limit)
    return tags

@router.get("/{tag_id}", response_model=Etiqueta)
def read_tag(tag_id: int, db: Session = Depends(get_db), current_user: Etiqueta = Depends(get_current_usuario)):
    db_tag = get_etiqueta(db, etiqueta_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    return db_tag

@router.put("/{tag_id}", response_model=Etiqueta)
def update_tag(tag_id: int, tag: EtiquetaCreate, db: Session = Depends(get_db), current_user: Etiqueta = Depends(get_current_usuario)):
    db_tag = get_etiqueta(db, etiqueta_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    return update_etiqueta(db=db, etiqueta_id=tag_id, etiqueta=tag)

@router.delete("/{tag_id}", response_model=Etiqueta)
def delete_tag(tag_id: int, db: Session = Depends(get_db), current_user: Etiqueta = Depends(get_current_usuario)):
    db_tag = get_etiqueta(db, etiqueta_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    return delete_etiqueta(db=db, etiqueta_id=tag_id)
