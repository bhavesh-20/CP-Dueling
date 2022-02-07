from fastapi import status
from sqlalchemy.sql.expression import insert, select

from app import db
from app.models import Friend, User
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

    @classmethod
    async def add_friend(cls, id, user):
        friend = await db.fetch_one(select([User]).where(User.id == id))
        if friend is None:
            return {
                "message": "User not found",
                "status_code": status.HTTP_404_NOT_FOUND,
            }
        friend_id = friend.id
        user_id = user.id
        if user_id == friend_id:
            return {
                "message": "You can't add yourself as a friend",
                "status_code": status.HTTP_400_BAD_REQUEST,
            }
        friend_exists = await db.fetch_one(
            select([Friend])
            .where(Friend.user_id == user_id)
            .where(Friend.friend_id == friend_id)
        )
        if friend_exists is not None:
            return {
                "message": "User already added",
                "status_code": status.HTTP_409_CONFLICT,
            }
        await db.execute(insert(Friend).values(user_id=user_id, friend_id=friend_id))
        return {
            "message": "User added",
            "status_code": status.HTTP_201_CREATED,
        }

    @classmethod
    async def get_friends(cls, user):
        friends = await db.fetch_all(select([Friend]).where(Friend.user_id == user.id))
        friends = await db.fetch_all(
            select([User]).where(User.id.in_(friend["friend_id"] for friend in friends))
        )
        return {
            "message": "Friends List",
            "data": [UserResponse(**friend) for friend in friends],
            "status_code": status.HTTP_200_OK,
        }
