from fastapi import APIRouter

from core.config import settings
from core.schemas.user import UserRead, UserCreate
from .fastapi_users import fastapi_users

router = APIRouter(prefix=settings.api.v1.users)
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
