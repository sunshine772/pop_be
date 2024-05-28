from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.sesion import Sesion, SesionCreate
from app.crud.sesion import create_sesion, get_sesion, get_sesiones, update_sesion, delete_sesion
from app.dependencies import get_db, get_current_usuario

router = APIRouter(
    prefix="/api/v1/sesiones",
    tags=["sesiones"]
)

@router.post("/", response_model=Sesion)
def create_session(sesion: SesionCreate, db: Session = Depends(get_db)):
    return create_sesion(db=db, sesion=sesion)

@router.get("/", response_model=list[Sesion])
def read_sessions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Sesion = Depends(get_current_usuario)):
    sessions = get_sesiones(db, skip=skip, limit=limit)
    return sessions

@router.get("/{session_id}", response_model=Sesion)
def read_session(session_id: int, db: Session = Depends(get_db), current_user: Sesion = Depends(get_current_usuario)):
    db_session = get_sesion(db, sesion_id=session_id)
    if db_session is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    return db_session

@router.put("/{session_id}", response_model=Sesion)
def update_session(session_id: int, sesion: SesionCreate, db: Session = Depends(get_db), current_user: Sesion = Depends(get_current_usuario)):
    db_session = get_sesion(db, sesion_id=session_id)
    if db_session is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    return update_sesion(db=db, sesion_id=session_id, sesion=sesion)

@router.delete("/{session_id}", response_model=Sesion)
def delete_session(session_id: int, db: Session = Depends(get_db), current_user: Sesion = Depends(get_current_usuario)):
    db_session = get_sesion(db, sesion_id=session_id)
    if db_session is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    return delete_sesion(db=db, sesion_id=session_id)
