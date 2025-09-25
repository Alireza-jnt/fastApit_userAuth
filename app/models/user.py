from typing import Optional
from pydantic import EmailStr, Field
from app.models.base import BaseDocument


class User(BaseDocument):
    """User Model

    This model represents a user in the system
    """

    # the "..." is FastApi way of doing required=True
    email: EmailStr = Field(..., unique=True)
    username: str = Field(..., min_length=3, max_length=50, unique=True)
    hashed_password: str
    full_name: Optional[str] = None
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "username": "johndoe",
                "full_name": "John Doe",
                "is_active": True,
                "is_superuser": False
            }
        }