from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.pelicula_etiqueta import PeliculaEtiqueta, PeliculaEtiquetaCreate
from app.crud.pelicula_etiqueta import create_pelicula_etiqueta, get_pelicula_etiqueta, get_peliculas_etiquetas, delete_pelicula_etiqueta
from app.dependencies import get_db, get_current_usuario

router = APIRouter(
    prefix="/api/v1/peliculas-etiquetas",
    tags=["peliculas-etiquetas"]
)

@router.post("/", response_model=PeliculaEtiqueta)
def create_movie_tag(movie_tag: PeliculaEtiquetaCreate, db: Session = Depends(get_db)):
    return create_pelicula_etiqueta(db=db, pelicula_etiqueta=movie_tag)

@router.get("/", response_model=list[PeliculaEtiqueta])
def read_movie_tags(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: PeliculaEtiqueta = Depends(get_current_usuario)):
    movie_tags = get_peliculas_etiquetas(db, skip=skip, limit=limit)
    return movie_tags

@router.get("/{movie_id}/{tag_id}", response_model=PeliculaEtiqueta)
def read_movie_tag(movie_id: int, tag_id: int, db: Session = Depends(get_db), current_user: PeliculaEtiqueta = Depends(get_current_usuario)):
    db_movie_tag = get_pelicula_etiqueta(db, pelicula_id=movie_id, etiqueta_id=tag_id)
    if db_movie_tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie tag not found")
    return db_movie_tag

@router.delete("/{movie_id}/{tag_id}", response_model=PeliculaEtiqueta)
def delete_movie_tag(movie_id: int, tag_id: int, db: Session = Depends(get_db), current_user: PeliculaEtiqueta = Depends(get_current_usuario)):
    db_movie_tag = get_pelicula_etiqueta(db, pelicula_id=movie_id, etiqueta_id=tag_id)
    if db_movie_tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie tag not found")
    return delete_pelicula_etiqueta(db=db, pelicula_id=movie_id, etiqueta_id=tag_id)
