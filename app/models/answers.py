from datetime import datetime
from enum import IntEnum

from pydantic import BaseModel, Field



class Answer(BaseModel):
    id: int = Field(..., description="Primary key - integer id of the Answer")
    body: str = Field(..., description="Answer of the user")
    created_by:str=Field(None,description="the creator of the Answer")
    created_at: datetime = Field(..., description="Datetime when the user submitted the Answer")
    is_blacklisted: bool = Field(False, description="Denotes if the Answer is blacklisted at the moment")
    upvotes: int=Field(...,description="Number of upvotes")
    downvotes: int=Field(...,description="Number of downvotes")  