from typing import List

from pydantic import BaseModel, Field


class RequestMeta(BaseModel):
    api: str = Field(..., description="API path")
    method: str = Field(..., description="API method name, like GET, POST, PUT, DELETE")
    body: dict = Field(..., description="JSON body received in the request (if any)")


class APIError(BaseModel):
    message: str = Field(..., description="Error message")
    stacktrace: List[str] = Field(..., description="Trace entries of the exception")
    request: RequestMeta = Field(..., description="Metadata associated with the request")


class ClientError(BaseModel):
    error: str = Field(..., description="Text description of client error")