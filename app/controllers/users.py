from fastapi import APIRouter, Depends, status

from app.jwt_dependency import get_current_user
from app.entities.errors import ClientError, APIError
from app.models.users import User

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