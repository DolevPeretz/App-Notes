
from typing import Optional
from pydantic import BaseModel, ConfigDict


class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteOut(NoteBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)
