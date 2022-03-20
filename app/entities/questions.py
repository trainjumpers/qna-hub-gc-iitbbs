import re

from pydantic import BaseModel, Field, validator

from app.constants import EMAIL_REGEX, PASSWORD_REGEX


class QuestionInput(BaseModel):
    body: str = Field(..., description="question of the user")

    def json(self, *args, **kwargs):
        return super(QuestionInput, self).json()
