from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.pelicula import Pelicula, PeliculaCreate
from app.crud.pelicula import create_pelicula, get_pelicula, get_peliculas, update_pelicula, delete_pelicula
from app.dependencies import get_db, get_current_usuario

router = APIRouter(
    prefix="/api/v1/peliculas",
    tags=["peliculas"]
)

@router.post("/", response_model=Pelicula)
def create_movie(movie: PeliculaCreate, db: Session = Depends(get_db)):
    return create_pelicula(db=db, pelicula=movie)

@router.get("/", response_model=list[Pelicula])
def read_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Pelicula = Depends(get_current_usuario)):
    movies = get_peliculas(db, skip=skip, limit=limit)
    return movies

@router.get("/{movie_id}", response_model=Pelicula)
def read_movie(movie_id: int, db: Session = Depends(get_db), current_user: Pelicula = Depends(get_current_usuario)):
    db_movie = get_pelicula(db, pelicula_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return db_movie

@router.put("/{movie_id}", response_model=Pelicula)
def update_movie(movie_id: int, movie: PeliculaCreate, db: Session = Depends(get_db), current_user: Pelicula = Depends(get_current_usuario)):
    db_movie = get_pelicula(db, pelicula_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return update_pelicula(db=db, pelicula_id=movie_id, pelicula=movie)

@router.delete("/{movie_id}", response_model=Pelicula)
def delete_movie(movie_id: int, db: Session = Depends(get_db), current_user: Pelicula = Depends(get_current_usuario)):
    db_movie = get_pelicula(db, pelicula_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return delete_pelicula(db=db, pelicula_id=movie_id)
