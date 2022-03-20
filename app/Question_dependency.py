from typing import Union, Dict

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import ExpiredSignatureError

from app.exceptions.client_request import UserUnauthorizedException
from app.models.users import User
from app.models.users import Question

from app.services.users import UserService
from app.services.questions import QuestionService
from app.utils.jwt import jwt_decode_token_to_user


async def get_all_question() -> list[Question]:

    return await QuestionService().fetch_all_question()


async def get_user_question(email: str) -> list[Question]:

    return await QuestionService().fetch_user_question(email)