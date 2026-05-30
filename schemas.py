from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    model_config = {
        "from_attributes": True
    }


class NoteCreate(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None