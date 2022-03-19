import os
from typing import Optional

from asyncpg import Pool, Record

from app.database import DatabaseConnectionPool
from app.exceptions.client_request import UserNotFoundException
from app.models.users import User
from app.utils.database import deserialize_records
from app.utils.logging import logger


class UserService:

    def __init__(self):
        self.pool: Pool = DatabaseConnectionPool.get_connection_pool()
        self.schema: str = os.environ.get('DB_SCHEMA')

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