from datetime import date, datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    jobs: list["Job"] = Relationship(back_populates="owner")

class JobBase(SQLModel):
    title: str
    company: str
    status: str = "applied"
    applied_date: Optional[date] = None
    link: Optional[str] = None
    notes: Optional[str] = None

class Job(JobBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Optional[User] = Relationship(back_populates="jobs")
