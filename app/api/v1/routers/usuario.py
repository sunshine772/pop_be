from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.usuario import Usuario, UsuarioCreate
from app.crud.usuario import create_usuario, get_usuario_by_username, get_usuarios, get_usuario, update_usuario, delete_usuario
from app.dependencies import get_db, get_current_usuario

router = APIRouter(
    prefix="/api/v1/usuarios",
    tags=["usuarios"]
)

@router.post("/", response_model=Usuario)
def create_user(user: UsuarioCreate, db: Session = Depends(get_db)):
    db_user = get_usuario_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    return create_usuario(db=db, usuario=user)

@router.get("/", response_model=list[Usuario])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_usuario)):
    users = get_usuarios(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=Usuario)
def read_user(user_id: int, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_usuario)):
    db_user = get_usuario(db, usuario_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=Usuario)
def update_user(user_id: int, user: UsuarioCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_usuario)):
    db_user = get_usuario(db, usuario_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return update_usuario(db=db, usuario_id=user_id, usuario=user)

@router.delete("/{user_id}", response_model=Usuario)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_usuario)):
    db_user = get_usuario(db, usuario_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return delete_usuario(db=db, usuario_id=user_id)
