from fastapi import status
from sqlalchemy.sql.expression import select

from app import db
from app.models import User
from app.schemas import UserResponse


class UserService:
    @classmethod
    async def get_user_by_id(cls, id):
        user = await db.fetch_one(select([User]).where(User.id == id))
        if user is None:
            return {
                "message": "User not found",
                "status_code": status.HTTP_404_NOT_FOUND,
            }

        return {
            "message": "User found",
            "data": UserResponse(**user),
            "status_code": status.HTTP_200_OK,
        }

    @classmethod
    async def get_user_by_name(cls, name):
        user = await db.fetch_one(select([User]).where(User.username == name))
        if user is None:
            return {
                "message": "User not found",
                "status_code": status.HTTP_404_NOT_FOUND,
            }
        return {
            "message": "User found",
            "data": UserResponse(**user),
            "status_code": status.HTTP_200_OK,
        }
