from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routers import (
    auth,
    usuario,
    sesion,
    imagen,
    pelicula,
    genero,
    etiqueta,
    pelicula_etiqueta,
    comentario,
)
from app.database.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye los routers
app.include_router(auth.router)
app.include_router(usuario.router)
app.include_router(sesion.router)
app.include_router(imagen.router)
app.include_router(pelicula.router)
app.include_router(genero.router)
app.include_router(etiqueta.router)
app.include_router(pelicula_etiqueta.router)
app.include_router(comentario.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie API"}
