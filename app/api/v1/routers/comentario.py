from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.comentario import Comentario, ComentarioCreate
from app.crud.comentario import create_comentario, get_comentario, get_comentarios, update_comentario, delete_comentario
from app.dependencies import get_db, get_current_usuario

router = APIRouter(
    prefix="/api/v1/comentarios",
    tags=["comentarios"]
)

@router.post("/", response_model=Comentario)
def create_comment(comment: ComentarioCreate, db: Session = Depends(get_db)):
    return create_comentario(db=db, comentario=comment)

@router.get("/", response_model=list[Comentario])
def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Comentario = Depends(get_current_usuario)):
    comments = get_comentarios(db, skip=skip, limit=limit)
    return comments

@router.get("/{comment_id}", response_model=Comentario)
def read_comment(comment_id: int, db: Session = Depends(get_db), current_user: Comentario = Depends(get_current_usuario)):
    db_comment = get_comentario(db, comentario_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    return db_comment

@router.put("/{comment_id}", response_model=Comentario)
def update_comment(comment_id: int, comment: ComentarioCreate, db: Session = Depends(get_db), current_user: Comentario = Depends(get_current_usuario)):
    db_comment = get_comentario(db, comentario_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    return update_comentario(db=db, comentario_id=comment_id, comentario=comment)

@router.delete("/{comment_id}", response_model=Comentario)
def delete_comment(comment_id: int, db: Session = Depends(get_db), current_user: Comentario = Depends(get_current_usuario)):
    db_comment = get_comentario(db, comentario_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    return delete_comentario(db=db, comentario_id=comment_id)
