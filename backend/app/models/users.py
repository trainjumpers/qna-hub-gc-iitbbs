from datetime import datetime
from enum import IntEnum

from pydantic import BaseModel, Field


class UserRole(IntEnum):
    REGULAR = 0
    ADMIN = 1


class User(BaseModel):
    id: int = Field(..., description="Primary key - integer id of the user")
    email: str = Field(..., description="Email id of the user")
    hashed_password: str = Field(..., description="Hash of the password entered by the user at signup")
    name: str = Field(None, description="Name of the user")
    role: UserRole = Field(None, description="User's role - 0 => Regular, 1 => Admin")
    is_verified: bool = Field(False, description="Denotes if the user's identity is verified by email")
    created_at: datetime = Field(..., description="Datetime when the user signed up to the platform")
    is_active: bool = Field(False, description="Denotes if the user is active at the moment")
    is_blacklisted: bool = Field(False, description="Denotes if the user is blacklisted at the moment")