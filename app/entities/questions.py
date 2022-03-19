import re

from pydantic import BaseModel, Field, validator

from app.constants import EMAIL_REGEX, PASSWORD_REGEX

class QuestionInput(BaseModel):
    body: str = Field(..., description="question of the user")
    created_by:str=Field(...,description="email of the user who has posted that particular question")
    def json(self, *args, **kwargs):
        return super(QuestionInput,self).json()