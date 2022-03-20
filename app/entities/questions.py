from pydantic import BaseModel, Field


class QuestionInput(BaseModel):
    title: str = Field(..., description="Title of the question")
    body: str = Field(..., description="question of the user")

    def json(self, *args, **kwargs):
        return super(QuestionInput, self).json()
