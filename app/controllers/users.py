import json
import traceback

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from app.entities.status import SuccessResponse

from app.jwt_dependency import get_current_user
from app.entities.users import *
from app.entities.errors import ClientError, APIError
from app.exceptions.client_request import UserUnauthorizedException
from app.models.users import User

from app.services.users import UserService
from app.utils.jwt import jwt_encode_user_to_token
from app.utils.password import get_password_hash, verify_password
from app.exceptions.api import APIException
from app.utils.logging import logger

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
        raise UserUnauthorizedException("Invalid credentials")
    try:
        auth_token: str = jwt_encode_user_to_token(user)
        return LoginOutput(access_token=auth_token, token_type="bearer")
    except Exception:
        data = {"email": form_data.username}
        raise APIException(trace=traceback.format_exc(), body=json.dumps(data))


@router.post(path="/signup",
             description="Register a new user",
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


@router.patch(path="",
              description="Update information about the user",
              status_code=status.HTTP_200_OK,
              response_model=User,
              response_model_exclude={'hashed_password'},
              responses={
                  status.HTTP_401_UNAUTHORIZED: {
                      "model": ClientError
                  },
                  status.HTTP_500_INTERNAL_SERVER_ERROR: {
                      "model": APIError
                  }
              })
async def patch_user(patch_user_input: PatchUserInput, user: User = Depends(get_user)):
    logger.info(f"Received request to update info for user: {user.id} with request body: {patch_user_input.json()}")

    fields_to_update: dict = patch_user_input.dict(exclude_none=True)
    if user.role is not None and patch_user_input.role and patch_user_input.role != user.role:
        logger.info(f"User: {user.id} has role {user.role}. Can't be changed to role {patch_user_input.role}")
        fields_to_update.pop('role')  # should not be updated once set

    if not fields_to_update:
        logger.info(f"Nothing to update for user: {user.id}")
        return user

    try:
        user: User = await UserService().update_fields(user.id, fields_to_update)
        logger.info(f"Successfully updated user info for user: {user.id}")
        return user
    except Exception:
        raise APIException(trace=traceback.format_exc(), body=patch_user_input.dict())


@router.patch(path="/password",
              description="Update password for a user",
              status_code=status.HTTP_200_OK,
              response_model=SuccessResponse,
              responses={
                  status.HTTP_401_UNAUTHORIZED: {
                      "model": ClientError
                  },
                  status.HTTP_500_INTERNAL_SERVER_ERROR: {
                      "model": APIError
                  }
              })
async def update_password(patch_password_input: PatchUserPasswordInput, user: User = Depends(get_user)):
    logger.info(f"Received request to update password for user: {user.id}")
    if not verify_password(patch_password_input.current_password, user.hashed_password):
        raise UserUnauthorizedException("Current password doesn't match")

    try:
        hashed_password: str = get_password_hash(patch_password_input.new_password)
        await UserService().update_fields(user.id, {"hashed_password": hashed_password})
        return SuccessResponse(message=f"Password was successfully updated for user: {user.id}")
    except Exception:
        raise APIException(trace=traceback.format_exc())