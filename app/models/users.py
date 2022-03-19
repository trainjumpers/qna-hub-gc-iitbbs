from datetime import datetime
from enum import IntEnum

from pydantic import BaseModel, Field


class UserRole(IntEnum):
    ADMIN = 1
    REGULAR = 0


class User(BaseModel):
    id: int = Field(..., description="Primary key - integer id of the user")
    email: str = Field(..., description="Email id of the user")
    hashed_password: str = Field(..., description="Hash of the password entered by the user at signup")
    name: str = Field(..., description="Name of the user")
    role: UserRole = Field(None, description="User's role - 0 => student, 1 => teacher")
    is_verified: bool = Field(False, description="Denotes if the user's identity is verified by email")
    created_at: datetime = Field(..., description="Datetime when the user signed up to the platform")
    is_active: bool = Field(False, description="Denotes if the user is active at the moment")
    is_blacklisted: bool = Field(False, description="Denotes if the user is blacklisted")