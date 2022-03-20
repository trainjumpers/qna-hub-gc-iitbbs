from datetime import datetime

from pydantic import BaseModel, Field


class Reply(BaseModel):
    id: int = Field(..., description="Primary key - integer id of the user")
    question_id: int = Field(..., desciption="Question id of the reply it is being given to")
    body: str = Field(..., description="reply of the question")
    created_by: str = Field(None, description="the creator of the question")
    created_at: datetime = Field(..., description="Datetime when the user submitted the question")
    is_blacklisted: bool = Field(False, description="Denotes if the question is blacklisted at the moment")
    upvotes: int = Field(0, description="Number of upvotes")
    downvotes: int = Field(0, description="Number of downvotes")
