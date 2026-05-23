from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Note, User
from app.schemas import NoteCreate, NoteResponse
from app.auth_utils import get_current_user

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.post("/", response_model=NoteResponse)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user_email: str = Depends(get_current_user)
):

    user = db.query(User).filter(
        User.email == current_user_email
    ).first()

    new_note = Note(
        title=note.title,
        content=note.content,
        owner_id=user.id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


@router.get("/", response_model=list[NoteResponse])
def get_notes(
    db: Session = Depends(get_db),
    current_user_email: str = Depends(get_current_user)
):

    user = db.query(User).filter(
        User.email == current_user_email
    ).first()

    notes = db.query(Note).filter(
        Note.owner_id == user.id
    ).all()

    return notes


@router.delete("/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user_email: str = Depends(get_current_user)
):

    user = db.query(User).filter(
        User.email == current_user_email
    ).first()

    note = db.query(Note).filter(
        Note.id == note_id
    ).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    if note.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(note)
    db.commit()

    return {"message": "Note deleted"}