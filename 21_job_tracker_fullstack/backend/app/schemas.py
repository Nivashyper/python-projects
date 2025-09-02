from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class JobCreate(BaseModel):
    title: str
    company: str
    status: str = "applied"
    applied_date: Optional[date] = None
    link: Optional[str] = None
    notes: Optional[str] = None

class JobRead(JobCreate):
    id: int
