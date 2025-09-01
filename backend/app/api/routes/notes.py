# app/api/routes/notes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import SessionLocal
from app.crud import note as note_crud
from app.schemas.note import NoteCreate, NoteUpdate, NoteOut
from app.db.models.note import Note
from app.db.models.user import User

from app.api.deps import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[NoteOut])
def get_notes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return note_crud.get_notes(db, user_id=current_user.id)


@router.post("/", response_model=NoteOut)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return note_crud.create_note(db, note, user_id=current_user.id)


@router.put("/{note_id}", response_model=NoteOut)
def update_note(
    note_id: int,
    update_data: NoteUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_note = note_crud.get_note_by_id(db, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    if db_note.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your note")
    return note_crud.update_note(db, db_note, update_data)


@router.delete("/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_note = note_crud.get_note_by_id(db, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    if db_note.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your note")
    note_crud.delete_note(db, db_note)
    return {"detail": "Note deleted"}
