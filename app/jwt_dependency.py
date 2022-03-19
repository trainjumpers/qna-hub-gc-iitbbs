from typing import Union, Dict

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import ExpiredSignatureError

from app.exceptions.client_request import UserUnauthorizedException
from app.models.users import User
from app.services.users import UserService
from app.utils.jwt import jwt_decode_token_to_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/accounts/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Bean used to authenticate a user via the bearer token.
    Validates the token by checking the expiration time and if it is valid fetches the user
    using the email id from the decoded token object.
    Args:
        token: string encoded jwt token generated on user login.
    Returns:
        user: pydantic model object of the user. See app.models.user.User.
    Raises:
        UserUnauthorizedException: when the user token has expired causing failure to decode the token.
    """

    try:
        user_dict: Dict[str, Union[int, str]] = jwt_decode_token_to_user(token)
        return await UserService().fetch_user(email=user_dict['email'])
    except ExpiredSignatureError:
        raise UserUnauthorizedException("Authentication token has expired")