from datetime import datetime
from enum import IntEnum

from pydantic import BaseModel, Field



class Question(BaseModel):
    id: int = Field(..., description="Primary key - integer id of the user")
    body: str = Field(..., description="Question of the user")
    created_by:str=Field(None,description="the creator of the question")
    created_at: datetime = Field(..., description="Datetime when the user submitted the question")
    is_blacklisted: bool = Field(False, description="Denotes if the question is blacklisted at the moment")
    answer: JSON=Field({},description="Stores all the answers for the question")
    upvotes: int=Field(0,description="Number of upvotes")
    downvotes: int=Field(0,description="Number of downvotes") 