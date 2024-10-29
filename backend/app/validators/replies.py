from app.exceptions.client_request import UserUnauthorizedException
from app.models.replies import Reply

from app.services.replies import ReplyService
from app.utils.logging import logger


class ReplyVailidator:

    def __init__(self, reply_id: int):
        self.reply_service: ReplyService = ReplyService()
        self.reply_id: int = reply_id
        self.reply: Reply | None = None

    async def init_reply(self):
        if not self.reply:
            self.reply = await self.reply_service.fetch_reply_with_id(self.reply_id)

    async def validate_reply_creator(self, user_email: str):
        """Validates if the user is creator of the reply.
        Performs a twofold validation:
        1. Checks if the reply exists or not.
        2. Checks if the user is the creator of the reply.
        Raises:
            ResourceNotFoundException: when reply with provided id is not found in the database.
            UserUnauthorizedException: when the user is not the creator of the reply.
        """

        logger.info(f"Validating if reply: {self.reply_id} exists and if user: {user_email} is the creator")

        await self.init_reply()
        if self.reply.created_by != user_email:
            raise UserUnauthorizedException(f"User: {user_email} is not creator of reply: {self.reply_id}.")

        logger.info(f"Reply: {self.reply_id} exists and user: {user_email} is the creator")