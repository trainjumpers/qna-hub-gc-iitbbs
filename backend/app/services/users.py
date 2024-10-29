from datetime import datetime
import os
from typing import Any, Dict, List, Tuple, Optional, Union

from asyncpg import Pool, Record

from app.database import DatabaseConnectionPool
from app.entities.users import SignupInput
from app.exceptions.client_request import UserNotFoundException
from app.models.users import User
from app.utils.database import deserialize_records
from app.utils.password import get_password_hash
from app.utils.logging import logger


class UserService:

    def __init__(self):
        self.pool: Pool = DatabaseConnectionPool.get_connection_pool()
        self.schema: str = os.environ.get('DB_SCHEMA')

    async def create_new_user(self, signup_input: SignupInput) -> User:
        """Creates a new user in the database.

        Args:
            signup_input: request body model object for the signup api

        Returns:
            user: pydantic model object of the user. See app.models.user.User
        """

        logger.info(f"Creating new user: {signup_input.json()}")
        query = f"INSERT INTO {self.schema}.user (email, hashed_password) VALUES ($1, $2) RETURNING *;"
        hashed_password = get_password_hash(signup_input.password)
        params: Tuple[str, str] = (signup_input.email, hashed_password)

        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to insert new user via query: {query}")
                user_record: Record = await connection.fetchrow(query, *params)

        logger.info(f"User: {signup_input.json()} successfully inserted in the db")
        return deserialize_records(user_record, User)

    async def fetch_user(self, email: str) -> User:
        """Fetches user with the provided email from the database.

        Args:
            email: email id of the user.

        Returns:
            user: pydantic model object of the user. See app.models.user.User.

        Raises:
            UserNotFoundException: when user with provided email is not found in the database.
        """

        query = f"SELECT * FROM {self.schema}.user WHERE email = $1;"

        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to fetch user via query: {query}")
                user_record: Optional[Record] = await connection.fetchrow(query, email)

        if not user_record:
            raise UserNotFoundException(email)
        return deserialize_records(user_record, User)

    async def update_fields(self, user_id: int, fields: Dict[str, Union[int, str, datetime]]) -> User:
        """Updates user with id as user_id with the provided fields.
        Args:
            user_id : id of the user.
            fields : a dictionary of fields with key as field name and value as attribute value
        Returns:
            user: pydantic model object of the updated user. See app.models.user.User
        """

        logger.info(f"Updating user fields: {fields}")
        params: List[Any] = [val for val in fields.values()]
        update_clause_items: List[str] = list(map(lambda x: f"{x[1]} = ${x[0] + 1}", enumerate(fields.keys())))
        update_clause: str = ", ".join(update_clause_items)
        query = f"UPDATE {self.schema}.user SET {update_clause} WHERE id = {user_id} RETURNING *;"
        logger.info(f"Updating with following query: {query}")

        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to patch user via query: {query}")
                user_record: Record = await connection.fetchrow(query, *params)

        logger.info(f"Successfully updated fields : {fields} for user: {user_id}")
        return deserialize_records(user_record, User)
