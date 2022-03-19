from typing import List
from dotenv import load_dotenv

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status

from app.exceptions.client_request_exception import ResourceNotFoundException, UserUnauthorizedException
from app.exceptions.api_exception import APIException

from app.utils.logging import logger

from database import DatabaseConnectionPool

app = FastAPI(title="GC Hackathon", version="1.0.0")


@app.get("/")
@app.add_middleware(CORSMiddleware,
                    allow_origins=["localhost:3000"],
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"])
@app.on_event('startup')
async def init():
    logger.info("Performing init tasks")
    loaded = load_dotenv(dotenv_path='.env')
    logger.info(f"Loaded .env file: {loaded}")
    await DatabaseConnectionPool.create_connection_pool()
    logger.info("Initialized database connection pool")


@app.on_event('shutdown')
async def finalise():
    await DatabaseConnectionPool.close_connection_pool()
    logger.info("Closed database connection pool")


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