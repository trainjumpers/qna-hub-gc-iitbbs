import os
from typing import List, Tuple, Optional

from asyncpg import Pool, Record

from app.database import DatabaseConnectionPool
from app.exceptions.client_request import ResourceNotFoundException
from app.entities.questions import QuestionInput
from app.models.questions import Question
from app.utils.database import deserialize_records
from app.utils.logging import logger


class QuestionService:

    def __init__(self):
        self.pool: Pool = DatabaseConnectionPool.get_connection_pool()
        self.schema: str = os.environ.get('DB_SCHEMA')

    async def create_new_question(self, question_input: list[QuestionInput]) -> Question:
        """Creates a new question in the database.

        Args:
            question_input: request body model object for the question api

        Returns:
            question: pydantic model object of the question. See app.models.question.Question
        """

        logger.info(f"Creating new question: {question_input.json()}")
        query = f"INSERT INTO {self.schema}.question (question) VALUES ($1,$2) RETURNING *;"
        params: Tuple[str, str] = (question_input.body, question_input.created_by)
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to insert new question via query: {query}")
                question_record: Record = await connection.fetchrow(query, *params)

        logger.info(f"Question: {question_input.json()} successfully inserted in the db")
        return deserialize_records(question_record, Question)

    async def fetch_all_question(self) -> List[Question]:

        query = f"SELECT * FROM {self.schema}.question"

        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to fetch all questions via query: {query}")
                question_record: Optional[Record] = await connection.fetch(query)

        return question_record

    async def fetch_user_question(self, email: str) -> List[Question]:

        query = f"SELECT * FROM {self.schema}.question where created_by=$1"

        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to fetch user questions via query: {query}")
                question_record: Optional[Record] = await connection.fetch(query, email)

        return question_record

    async def delete_quesiton(self, question_id: int) -> Question:

        query = f"DELETE FROM {self.schema}.question where id=$1 RETURNING *;"

        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to delete question via query: {query}")
                question_record: Optional[Record] = await connection.fetchrow(query, question_id)

        return question_record

    async def fetch_question_with_id(self, id: int) -> Question:

        query = f"SELECT * FROM {self.schema}.question where id=$1"

        async with self.pool.acquire() as connection:
            async with connection.transaction():
                logger.info(f"Acquired connection and opened transaction to fetch user questions via query: {query}")
                question_record: Optional[Record] = await connection.fetch(query, id)

        if not question_record:
            raise ResourceNotFoundException("Question with id {id} not found")

        return question_record