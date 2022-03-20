from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, Json


class Question(BaseModel):
    id: int = Field(..., description="Primary key - integer id of the user")
    body: str = Field(..., description="Question of the user")
    created_by: str = Field(None, description="the creator of the question")
    created_at: datetime = Field(..., description="Datetime when the user submitted the question")
    is_blacklisted: bool = Field(False, description="Denotes if the question is blacklisted at the moment")
    answer: List[int] = Field([], description="Stores all the answers for the question")
    upvotes: int = Field(0, description="Number of upvotes")
    downvotes: int = Field(0, description="Number of downvotes")
