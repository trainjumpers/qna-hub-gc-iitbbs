import os
from datetime import datetime, timedelta
from typing import Dict, Union

import jwt

from app.models.users import User


def jwt_encode_user_to_token(user: User) -> str:
    """Encodes the provided user object into a json web token.
    The default expiration time is one day from the current time.
    Args:
        user: pydantic model object of the user. See app.models.user.User.
    Returns:
        token: encoded string jwt token for the user session.
    """

    expiration_time: datetime = datetime.now() + timedelta(days=1)
    data: Dict[str, Union[str, int]] = {"id": user.id, "email": user.email, "exp": expiration_time}
    secret_key = os.environ.get("ENCODING_KEY")
    return jwt.encode(data, secret_key, algorithm="HS256")


def jwt_decode_token_to_user(token: str) -> Dict[str, Union[str, int]]:
    """Decodes the provided json web token.
    Args:
        token: encoded string jwt token associated with a user session
    Returns:
        user_dict: dictionary containing the user id and user email to uniquely identify the associated user.
    Raises:
        ExpiredSignatureError: when the 'exp' property holds a timestamp which has already passed.
    """

    secret_key = os.environ.get("ENCODING_KEY")
    user_dict: Dict[str, Union[str, int]] = jwt.decode(token, secret_key, algorithms=["HS256"])
    return user_dict