from typing import Optional, List, Set
from app.exceptions.client_request import UserUnauthorizedException
from app.models.questions import Question

from app.models.users import UserRole
from app.services.questions import QuestionService
from app.utils.logging import logger


class QuestionValidator:

    def __init__(self, question_id: int):
        self.question_service: QuestionService = QuestionService()
        self.question_id: int = question_id
        self.question: Question | None = None

    async def init_question(self):
        if not self.question:
            self.question = await self.question_service.fetch_question_with_id(self.question_id)

    async def validate_question_creator(self, user_email: str):
        """Validates if the user is creator of the question.
        Performs a twofold validation:
        1. Checks if the question exists or not.
        2. Checks if the user is the creator of the question.
        Raises:
            ResourceNotFoundException: when question with provided id is not found in the database.
            UserUnauthorizedException: when the user is not the creator of the question.
        """

        logger.info(f"Validating if question: {self.question_id} exists and if user: {user_email} is the creator")

        await self.init_question()
        if self.question.created_by != user_email:
            raise UserUnauthorizedException(f"User: {user_email} is not creator of question: {self.question_id}.")

        logger.info(f"question: {self.question_id} exists and user: {user_email} is the creator")