from pydantic import BaseModel, Field

from app.constants import EMAIL_REGEX, PASSWORD_REGEX


class ReplyInput(BaseModel):
    body: str = Field(..., description="reply of the question")

    def json(self, *args, **kwargs):
        return super(ReplyInput, self).json()
