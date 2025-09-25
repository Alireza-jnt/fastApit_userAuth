from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base schema for User"""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: Optional[str] = None
    is_active: bool = True


class UserCreate(UserBase):
    """Schema for creating a new user"""
    password: str = Field(..., min_length=6)


class UserUpdate(BaseModel):
    """Schema for updating user information"""
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = None
    password: Optional[str] = Field(None, min_length=6)
    is_active: Optional[bool] = None


class UserInDB(UserBase):
    """Schema for user stored in database"""
    id: str
    hashed_password: str
    is_superuser: bool = False

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    """Schema for user response (public information)"""
    id: str
    email: str
    username: str
    full_name: Optional[str]
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True


class PasswordChange(BaseModel):
    """Schema for password change request"""
    current_password: str
    new_password: str = Field(..., min_length=6)


class UserList(BaseModel):
    """Schema for listing multiple users"""
    users: list[UserResponse]
    total: int
    page: int
    page_size: int