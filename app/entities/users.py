from datetime import date
import re

from pydantic import BaseModel, Field, validator

from app.constants import EMAIL_REGEX, PASSWORD_REGEX
from app.models.users import UserRole


class LoginInput(BaseModel):
    email: str = Field(..., description="Email ID of the user signing in to the platform")
    password: str = Field(..., description="Text password of the user signing in to the platform")

    @validator("email")
    def validate_email(cls, email: str):
        email = email.lower().strip()
        if not email:
            raise ValueError("Email is empty")
        if not re.match(EMAIL_REGEX, email):
            raise ValueError(f"Email: {email} is not a valid email address")
        return email  # return a validated value

    @validator("password")
    def validate_password(cls, password: str):
        password = password.strip()
        if not password:
            raise ValueError("Password is empty")
        if len(password) < 8:
            raise ValueError("Password cannot be less than 8 characters long")
        if not re.match(PASSWORD_REGEX, password):
            special_characters = '!@#$%&*-+(){}_'
            raise ValueError(f"Password should be alphanumeric and contain only one of {special_characters}")
        return password


class LoginOutput(BaseModel):
    access_token: str = Field(..., description="Authentication token to associate with the user for all the APIs")
    token_type: str = Field(..., description="Type of the authentication token")


class SignupInput(LoginInput):

    def json(self, *args, **kwargs):  # overriding parent json() method to exclude password in the serialised object
        return super(SignupInput, self).json(exclude={"password"})


class PatchUserInput(BaseModel):
    role: UserRole = Field(None, description="User's role - 0 => student, 1 => teacher")
    name: str = Field(None, description='Name of the user')
    is_verified: bool = Field(None, description="Whether the user is verified or not")
    is_blacklisted: bool = Field(None, description="Whether the user is blacklisted or not")
    is_active: bool = Field(None, description="Whether the user is active or not")


class PatchUserPasswordInput(BaseModel):
    current_password: str = Field(..., description="Current password of the user")
    new_password: str = Field(..., description="New password of the user")

    @validator("new_password")
    def validate_new_password(cls, password: str):
        password = password.strip()
        if not password:
            raise ValueError("Password is empty")
        if len(password) < 8:
            raise ValueError("Password cannot be less than 8 characters long")
        if not re.match(PASSWORD_REGEX, password):
            special_characters = '!@#$%&*-+(){}_'
            raise ValueError(f"Password should be alphanumeric and contain only one of {special_characters}")
        return password
