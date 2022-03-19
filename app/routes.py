from fastapi import APIRouter
from app.controllers import users
"""
    This file includes all the various routers we write for the backend. Most of the routers go into the controller folder
    and that is what we will be importing for our use case.
"""

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])