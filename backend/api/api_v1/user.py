from fastapi import APIRouter

from core.schemas.user import UserRead, UserCreate
from .fastapi_users import fastapi_users

router = APIRouter()
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
