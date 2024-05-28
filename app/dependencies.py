from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal, get_db
from app.auth.jwt_bearer import JWTBearer
from app.auth.jwt_handler import decode_jwt
from app.crud.usuario import get_usuario
from app.crud.token import get_token

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_usuario(db: Session = Depends(get_db), token: str = Depends(JWTBearer())):
    try:
        payload = decode_jwt(token)
        usuario_id: int = payload.get("usuario_id")
        if usuario_id is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid authentication credentials",
            )
        token_db = get_token(db, access_token=token)
        if not token_db or not token_db.estado:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid or inactive token",
            )
        usuario = get_usuario(db, usuario_id=usuario_id)
        if usuario is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return usuario
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Invalid authentication credentials: {e}",
        )
