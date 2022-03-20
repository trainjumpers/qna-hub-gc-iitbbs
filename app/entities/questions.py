import re
from turtle import title

from pydantic import BaseModel, Field, validator

from app.constants import EMAIL_REGEX, PASSWORD_REGEX


class QuestionInput(BaseModel):
    title: str = Field(..., description="Title of the question")
    body: str = Field(..., description="question of the user")

    def json(self, *args, **kwargs):
        return super(QuestionInput, self).json()
