from pydantic import BaseModel, Field


class SuccessResponse(BaseModel):
    message: str = Field(..., description="Text description of success message")