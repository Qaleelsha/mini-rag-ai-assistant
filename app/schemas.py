# app/schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional

# Auth schemas
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Document schemas
class DocumentCreate(BaseModel):
    title: str
    content: Optional[str] = None  # for text or parsed PDF content

class DocumentResponse(BaseModel):
    id: int
    title: str
    filename: Optional[str]
    content: str

    class Config:
        orm_mode = True