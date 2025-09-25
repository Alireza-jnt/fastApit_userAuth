from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    """Schema for login request"""

    username: str = Field(..., description="Username or email")
    password: str = Field(..., min_length=6)


class RegisterRequest(BaseModel):
    """Schema for registration request"""

    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)
    full_name: str = Field(None)


class TokenResponse(BaseModel):
    """Schema for token response"""
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    """Schema for user information response"""

    id: str
    email: str
    username: str
    full_name: Optional[str]
    is_active: bool

    class Config:
        from_attributes = True
