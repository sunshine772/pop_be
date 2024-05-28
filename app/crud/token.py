from sqlalchemy.orm import Session
from app.models.token import Token
from app.schemas.token import TokenCreate

def create_token(db: Session, token: TokenCreate):
    db_token = Token(
        access_token=token.access_token,
        refresh_token=token.refresh_token,
        usuario_id=token.usuario_id
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

def get_token(db: Session, access_token: str):
    return db.query(Token).filter(Token.access_token == access_token).first()

def get_tokens(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Token).offset(skip).limit(limit).all()

def update_token(db: Session, access_token: str, token: Token):
    db_token = get_token(db, access_token)
    if db_token:
        db_token.refresh_token = token.refresh_token
        db_token.estado = token.estado
        db.commit()
        db.refresh(db_token)
    return db_token

def delete_token(db: Session, access_token: str):
    db_token = get_token(db, access_token=access_token)
    if db_token:
        db.delete(db_token)
        db.commit()
    return db_token
