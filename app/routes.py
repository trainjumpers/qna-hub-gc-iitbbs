from fastapi import APIRouter

from app.controllers import questions, users

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(questions.router, prefix="/questions", tags=["questions"])
