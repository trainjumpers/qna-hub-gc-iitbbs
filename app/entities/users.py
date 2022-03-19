import re

from pydantic import BaseModel, Field, validator

from app.constants import EMAIL_REGEX, PASSWORD_REGEX


class LoginInput(BaseModel):
    email: str = Field(..., description="Email ID of the user signing in")
    password: str = Field(..., description="Text password of the user signing in")

    @validator("email")
    def validate_email(cls, email: str):
        email = email.lower().strip()
        if not email:
            raise ValueError("Email is empty")
        if not re.match(EMAIL_REGEX, email):
            raise ValueError(f"Email: {email} is not a valid email address")
        return email

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
    name: str = Field(..., description="Name of the user signing up")

    @validator("name")
    def validate_name(cls, name: str):
        name = name.strip()
        if not name:
            raise ValueError(f"Name is empty")
        return name

    def json(self, *args, **kwargs):  # overriding parent json() method to exclude password in the serialised object
        return super(SignupInput, self).json(exclude={"password"})