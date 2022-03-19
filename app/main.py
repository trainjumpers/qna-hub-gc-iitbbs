from typing import List

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import status

from app.exceptions.client_request_exception import ResourceNotFoundException, UserUnauthorizedException
from app.exceptions.api_exception import APIException

app = FastAPI(title="GC Hackathon", version="1.0.0")


@app.get("/")
async def root():
    return {
        "message": "Welcome to our discussion forum meant for GC Hackathon participants and a few special creatures"
    }


@app.exception_handler(APIException)
async def global_api_exception_handler(request: Request, exc: APIException):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=exc.get_context_dict(request))


@app.exception_handler(RequestValidationError)
async def global_validation_exception_handler(_: Request, exc: RequestValidationError):
    error_messages: List[str] = list(map(lambda x: x["msg"], exc.errors()))
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"errors": error_messages})


@app.exception_handler(ResourceNotFoundException)
async def global_resource_not_found_exception_handler(_: Request, exc: ResourceNotFoundException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": str(exc)})


@app.exception_handler(UserUnauthorizedException)
async def global_user_unauthorized_exception_handler(_: Request, exc: UserUnauthorizedException):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"error": str(exc)})