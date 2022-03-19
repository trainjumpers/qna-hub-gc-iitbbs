import json
import traceback

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.jwt_dependency import get_current_user,get_all_question
from app.jwt_dependency import get_current_question
from app.entities.users import *
from app.entities.errors import ClientError, APIError
from app.exceptions.client_request import UserUnauthorizedException
from app.models.users import User
from app.models.questions import Question
from app.services.users import UserService
from app.services.questions import QuestionService
from app.utils.jwt import jwt_encode_user_to_token
from app.utils.password import verify_password
from app.exceptions.api import APIException
from app.utils.logging import logger

router: APIRouter = APIRouter()
@router.get(path="/AllQuestion",
            description="Fetch all the current questions",
            status_code=status.HTTP_200_OK,
            response_model=Question,
            responses={
                status.HTTP_401_UNAUTHORIZED: {
                    "model": ClientError
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": ClientError
                },
                status.HTTP_500_INTERNAL_SERVER_ERROR: {
                    "model": APIError
                }
            })
async def get_all_questions(question: Question = Depends(get_all_question)):
    return question
@router.get(path="/UserQuestion",
            description="Fetch all the current questions",
            status_code=status.HTTP_200_OK,
            response_model=Question,
            responses={
                status.HTTP_401_UNAUTHORIZED: {
                    "model": ClientError
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": ClientError
                },
                status.HTTP_500_INTERNAL_SERVER_ERROR: {
                    "model": APIError
                }
            })
async def get_question(question: Ques):
    return question
@router.post(path="/Question",
             description="Post a question",
             status_code=status.HTTP_201_CREATED,
             response_model=Question,
             responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {
                 "model": APIError
             }})
async def ask(question_input: QuestionInput):
    logger.info(f"Received question request with payload: {question_input.json()}")
    try:
        question: Question = await QuestionService().create_new_question(question_input)
        logger.info(f"Question created successfully")
        return question
    except Exception:
        raise APIException(trace=traceback.format_exc(), body=question_input.json())