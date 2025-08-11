from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl

class User(BaseModel):
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar: Optional[HttpUrl] = None