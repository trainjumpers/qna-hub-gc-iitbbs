from pydantic import BaseModel, Field


class QuestionInput(BaseModel):
    title: str = Field(..., description="Title of the question")
    body: str = Field(..., description="question of the user")

    def json(self, *args, **kwargs):
        return super(QuestionInput, self).json()


class PatchQuestionInput(BaseModel):
    title: str = Field(None, description="Title of the question")
    body: str = Field(None, description='Body of the question')
    upvotes: int = Field(None, description="Upvote a question")
    downvotes: int = Field(None, description="Downvote a question")
