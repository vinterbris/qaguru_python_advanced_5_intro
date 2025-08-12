from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import BaseModel, EmailStr, HttpUrl

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr = None
    first_name: str = None
    last_name: str = None
    avatar: str = None