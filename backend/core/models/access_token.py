from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.types.user_id import UserIdType
from .base import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[int]):
    user_id: Mapped[UserIdType] = mapped_column(
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, AccessToken)
