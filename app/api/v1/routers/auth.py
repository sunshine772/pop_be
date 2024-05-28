from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.auth.jwt_handler import create_access_token, create_refresh_token
from app.auth.hash import verify_password
from app.models.usuario import Usuario
from app.schemas.token import Token, TokenCreate
from app.crud.usuario import get_usuario_by_username
from app.crud.token import create_token, delete_token, get_token
from app.database.connection import get_db
from app.utils.config import get_settings
from app.auth.jwt_bearer import JWTBearer
from app.dependencies import get_current_usuario

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["authentication"]
)

@router.post("/login", response_model=Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_usuario_by_username(db, username=form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    settings = get_settings()
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username, "usuario_id": user.usuario_id}, expires_delta=access_token_expires)
    refresh_token = create_refresh_token(data={"sub": user.username, "usuario_id": user.usuario_id})
    token_type="bearer"
    token_data = TokenCreate(access_token=access_token, refresh_token=refresh_token, usuario_id=user.usuario_id, token_type=token_type)
    create_token(db, token_data)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": token_type}

@router.post("/logout", dependencies=[Depends(JWTBearer())])
async def logout(request: Request, current_user: Usuario = Depends(get_current_usuario), db: Session = Depends(get_db)):
    token = request.headers.get('Authorization').split(" ")[1]
    stored_token = get_token(db, access_token=token)
    if stored_token:
        delete_token(db, access_token=stored_token.access_token)
    return {"msg": "Successfully logged out"}