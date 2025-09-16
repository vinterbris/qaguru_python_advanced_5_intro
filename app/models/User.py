from sqlmodel import SQLModel, Field
from pydantic import BaseModel, EmailStr, HttpUrl

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr
    first_name: str
    last_name: str
    avatar: str

class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl

class UserUpdate(BaseModel):
    email: EmailStr = None
    first_name: str = None
    last_name: str = None
    avatar: HttpUrl = None
