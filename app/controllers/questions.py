import traceback

from fastapi import APIRouter, Depends, status
from app.Question_dependency import get_all_question, get_user_question
from app.controllers.users import get_user
from app.entities.users import *
from app.entities.questions import QuestionInput
from app.entities.errors import ClientError, APIError
from app.models.users import User
from app.models.questions import Question
from app.services.questions import QuestionService
from app.exceptions.api import APIException
from app.utils.logging import logger

router: APIRouter = APIRouter()


@router.get(path="",
            description="Fetch all the questions",
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
async def get_all_questions(question: list[Question] = Depends(get_all_question)):
    return question


@router.get(path="/UserQuestion",
            description="Fetch all the questions created by a user",
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
async def get_question(question: list[Question] = Depends(get_user_question)):
    return question


@router.delete(path="/{question_id}",
               description="Delete the question",
               status_code=status.HTTP_200_OK,
               response_model=Question,
               responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {
                   "model": APIError
               }})
async def ask(question_id: int, user: User = Depends(get_user)):
    logger.info(f"Received question request with question id: {question_id}")
    try:
        question: Question = await QuestionService().delete_question(question_id)
        logger.info(f"Question created successfully")
        return question
    except Exception:
        raise APIException(trace=traceback.format_exc(), body=question_id)


@router.post(path="",
             description="Post a question",
             status_code=status.HTTP_201_CREATED,
             response_model=Question,
             responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {
                 "model": APIError
             }})
async def ask(question_input: list[QuestionInput]):
    logger.info(f"Received question request with payload: {question_input.json()}")
    try:
        question: Question = await QuestionService().create_new_question(question_input)
        logger.info(f"Question created successfully")
        return question
    except Exception:
        raise APIException(trace=traceback.format_exc(), body=question_input.json())