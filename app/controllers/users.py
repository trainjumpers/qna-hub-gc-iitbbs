import json
import traceback

from fastapi import APIRouter, Depends, status
from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.entities.errors import ClientError, APIError
from app.entities.users import LoginOutput, SignupInput
from app.exceptions.api import APIException
from app.exceptions.client_request import UserUnauthorizedException
from app.models.users import User
from app.services.users import UserService
from app.utils.jwt import jwt_encode_user_to_token
from app.utils.logging import logger
from app.utils.password import verify_password

from app.jwt_dependency import get_current_user

router: APIRouter = APIRouter()


@router.get(path="",
            description="Fetch currently logged user",
            status_code=status.HTTP_200_OK,
            response_model=User,
            response_model_exclude={'hashed_password'},
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
async def get_user(user: User = Depends(get_current_user)):
    return user


@router.post(path="/login",
             description="Sign in an existing user",
             status_code=status.HTTP_200_OK,
             response_model=LoginOutput,
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
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    logger.info(f"Received login request for user: {form_data.username}")
    user: User = await UserService().fetch_user(form_data.username)
    if not verify_password(form_data.password, user.hashed_password):
        raise UserUnauthorizedException("Invalid creds")
    try:
        auth_token: str = jwt_encode_user_to_token(user)
        return LoginOutput(access_token=auth_token, token_type="bearer")
    except Exception:
        data = {"email": form_data.username}
        raise APIException(trace=traceback.format_exc(), body=json.dumps(data))


@router.post(path="/signup",
             description="Register a user",
             status_code=status.HTTP_201_CREATED,
             response_model=User,
             response_model_exclude={'hashed_password'},
             responses={status.HTTP_500_INTERNAL_SERVER_ERROR: {
                 "model": APIError
             }})
async def signup(signup_input: SignupInput):
    logger.info(f"Received signup request with payload: {signup_input.json()}")
    try:
        user: User = await UserService().create_new_user(signup_input)
        logger.info(f"User successfully signed up")
        return user
    except Exception:
        raise APIException(trace=traceback.format_exc(), body=signup_input.json())