import os
from typing import List, Tuple

from asyncpg import Pool, Record

from app.database import DatabaseConnectionPool
from app.entities.replies import ReplyInput
from app.exceptions.client_request import ResourceNotFoundException
from app.models.replies import Reply
from app.utils.database import deserialize_records
from app.utils.logging import logger


class ReplyService:

    def __init__(self):
        self.pool: Pool = DatabaseConnectionPool.get_connection_pool()
        self.schema: str = os.environ.get('DB_SCHEMA')

    async def create_new_reply(self, reply_input: ReplyInput, email: str) -> Reply:
        """Creates a new reply in the database.

        Args:
            reply_input: request body model object for the reply api

        Returns:
            reply: pydantic model object of the reply. See app.models.reply.Reply
        """

        logger.info(f"Creating new reply: {reply_input.json()}")
        query = f"INSERT INTO {self.schema}.reply (reply) VALUES ($1,$2) RETURNING *;"
        params: Tuple[str, str] = (reply_input.body, email)
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to insert new reply via query: {query}")
                reply_record: Record = await connection.fetchrow(query, *params)

        logger.info(f"Reply: {reply_input.json()} successfully inserted in the db")
        return deserialize_records(reply_record, Reply)

    async def fetch_all_replies(self, question_id: int) -> List[Reply]:

        query = f"SELECT * FROM {self.schema}.reply WHERE question_id=$1"

        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to fetch all replies via query: {query}")
                reply_record: Record | None = await connection.fetch(query, question_id)

        return reply_record

    async def delete_reply(self, reply_id: int) -> Reply:

        query = f"DELETE FROM {self.schema}.reply where id=$1 RETURNING *;"

        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to delete reply via query: {query}")
                reply_record: Record | None = await connection.fetchrow(query, reply_id)

        return reply_record

    async def fetch_reply_with_id(self, id: int) -> Reply:

        query = f"SELECT * FROM {self.schema}.reply where id=$1"

        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to fetch user replys via query: {query}")
                reply_record: Record | None = await connection.fetch(query, id)

        if not reply_record:
            raise ResourceNotFoundException("reply with id {id} not found")

        return reply_record