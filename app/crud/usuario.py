from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.auth.hash import get_password_hash, verify_password

def get_usuario_by_username(db: Session, username: str):
    return db.query(Usuario).filter(Usuario.username == username).first()

def create_usuario(db: Session, usuario: UsuarioCreate):
    hashed_password = get_password_hash(usuario.password)
    db_usuario = Usuario(
        username=usuario.username,
        password=hashed_password,
        email=usuario.email,
        estado=usuario.estado,
        is_admin=usuario.is_admin
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Usuario).offset(skip).limit(limit).all()

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()

def update_usuario(db: Session, usuario_id: int, usuario: UsuarioCreate):
    db_usuario = db.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()
    if db_usuario:
        db_usuario.username = usuario.username
        db_usuario.email = usuario.email
        db_usuario.estado = usuario.estado
        db_usuario.is_admin = usuario.is_admin
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(Usuario).filter(Usuario.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user