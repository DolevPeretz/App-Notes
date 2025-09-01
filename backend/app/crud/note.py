
from sqlalchemy.orm import Session
from app.db.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate
from typing import List, Optional

def create_note(db: Session, note: NoteCreate, user_id: int) -> Note:
    db_note = Note(title=note.title, content=note.content,user_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_notes(db: Session, user_id: int) -> List[Note]:
    return db.query(Note).filter(Note.user_id == user_id).all()

def get_note_by_id(db: Session, note_id: int) -> Optional[Note]:
    return db.query(Note).filter(Note.id == note_id).first()

def update_note(db: Session, db_note: Note, update_data: NoteUpdate) -> Note:
    if update_data.title is not None:
        db_note.title = update_data.title
    if update_data.content is not None:
        db_note.content = update_data.content
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, db_note: Note):
    db.delete(db_note)
    db.commit()
