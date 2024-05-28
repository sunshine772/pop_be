from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.genero import Genero, GeneroCreate
from app.crud.genero import create_genero, get_genero, get_generos, update_genero, delete_genero
from app.dependencies import get_db, get_current_usuario

router = APIRouter(
    prefix="/api/v1/generos",
    tags=["generos"]
)

@router.post("/", response_model=Genero)
def create_genre(genre: GeneroCreate, db: Session = Depends(get_db), current_user: Genero = Depends(get_current_usuario)):
    return create_genero(db=db, genero=genre)

@router.get("/", response_model=list[Genero])
def read_genres(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Genero = Depends(get_current_usuario)):
    genres = get_generos(db, skip=skip, limit=limit)
    return genres

@router.get("/{genre_id}", response_model=Genero)
def read_genre(genre_id: int, db: Session = Depends(get_db), current_user: Genero = Depends(get_current_usuario)):
    db_genre = get_genero(db, genero_id=genre_id)
    if db_genre is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found")
    return db_genre

@router.put("/{genre_id}", response_model=Genero)
def update_genre(genre_id: int, genre: GeneroCreate, db: Session = Depends(get_db), current_user: Genero = Depends(get_current_usuario)):
    db_genre = get_genero(db, genero_id=genre_id)
    if db_genre is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found")
    return update_genero(db=db, genero_id=genre_id, genero=genre)

@router.delete("/{genre_id}", response_model=Genero)
def delete_genre(genre_id: int, db: Session = Depends(get_db), current_user: Genero = Depends(get_current_usuario)):
    db_genre = get_genero(db, genero_id=genre_id)
    if db_genre is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found")
    return delete_genero(db=db, genero_id=genre_id)
