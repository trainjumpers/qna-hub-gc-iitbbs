import asyncio
import traceback

from fastapi import APIRouter, Depends, status
from app.controllers.users import get_user
from app.entities.users import *
from app.entities.questions import QuestionInput
from app.entities.errors import ClientError, APIError
from app.models.users import User
from app.models.questions import Question
from app.services.questions import QuestionService
from app.exceptions.api import APIException
from app.utils.logging import logger
from app.validators.question import QuestionValidator

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
async def get_all_questions(user: User = Depends(get_user)):
    questions: list[Question] = await QuestionService().fetch_all_question()
    return questions


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
async def get_question(user: User = Depends(get_user)):
    questions: list[Question] = await QuestionService().fetch_user_question(user.email)
    return questions


@router.delete(path="/{question_id}",
               description="Delete the question",
               status_code=status.HTTP_200_OK,
               response_model=Question,
               responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {
                   "model": APIError
               }})
async def delete_question(question_id: int, user: User = Depends(get_user)):
    logger.info(f"Received question request with question id: {question_id}")
    validator: QuestionValidator = QuestionValidator(question_id)
    asyncio.gather(validator.validate_question_creator(user.email))
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
async def create_question(question_input: QuestionInput, user: User = Depends(get_user)):
    logger.info(f"Received question request with payload: {question_input.json()}")
    try:
        question: Question = await QuestionService().create_new_question(question_input, user.email)
        logger.info(f"Question created successfully")
        return question
    except Exception:
        raise APIException(trace=traceback.format_exc(), body=question_input.json())