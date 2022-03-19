from fastapi import APIRouter

from app.controllers import users

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
