import asyncio
import traceback

from fastapi import APIRouter, Depends, status
from app.controllers.users import get_user
from app.entities.replies import ReplyInput
from app.entities.users import *
from app.entities.errors import ClientError, APIError
from app.models.replies import Reply
from app.models.users import User
from app.exceptions.api import APIException
from app.services.replies import ReplyService
from app.utils.logging import logger
from app.validators.replies import ReplyVailidator

router: APIRouter = APIRouter()


@router.get(path="/{question_id}",
            description="Fetch all the replies",
            status_code=status.HTTP_200_OK,
            response_model=Reply,
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
async def get_all_replies(question_id: int, user: User = Depends(get_user)):
    questions: list[Reply] = await ReplyService().fetch_all_replies(question_id)
    return questions


@router.delete(path="/{reply_id}",
               description="Delete the reply",
               status_code=status.HTTP_200_OK,
               response_model=Reply,
               responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {
                   "model": APIError
               }})
async def delete_reply(reply_id: int, user: User = Depends(get_user)):
    logger.info(f"Received question request with reply id: {reply_id}")
    validator: ReplyVailidator = ReplyVailidator(reply_id)
    asyncio.gather(validator.validate_reply_creator(user.email))
    try:
        reply: Reply = await ReplyService().delete_reply(reply_id)
        logger.info(f"reply created successfully")
        return reply
    except Exception:
        raise APIException(trace=traceback.format_exc(), body=reply_id)


@router.post(path="",
             description="Post a reply",
             status_code=status.HTTP_201_CREATED,
             response_model=Reply,
             responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {
                 "model": APIError
             }})
async def create_reply(question_input: ReplyInput, user: User = Depends(get_user)):
    logger.info(f"Received question request with payload: {question_input.json()}")
    try:
        question: Reply = await ReplyService().create_new_question(question_input, user.email)
        logger.info(f"Question created successfully")
        return question
    except Exception:
        raise APIException(trace=traceback.format_exc(), body=question_input.json())