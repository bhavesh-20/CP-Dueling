from fastapi import status
from sqlalchemy.sql.expression import delete, insert, select

from app import db
from app.models import FriendRequests, Friends, User
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
    async def send_friend_request(cls, id, user):
        friend = await cls.get_user_by_id(id)
        if friend["status_code"] == status.HTTP_404_NOT_FOUND:
            return friend

        friend_id = friend["data"].id
        user_id = user.id
        if user_id == friend_id:
            return {
                "message": "You can't add yourself as a friend",
                "status_code": status.HTTP_400_BAD_REQUEST,
            }

        check_existing_request = await UserService.check_exsisting_request(
            user_id, friend_id
        )
        if check_existing_request is not None:
            return check_existing_request
        check_existing_request = await UserService.check_exsisting_request(
            friend_id, user_id
        )
        if check_existing_request is not None:
            return check_existing_request

        friend_exists = await db.fetch_one(
            select([Friends])
            .where(Friends.user_id == user_id)
            .where(Friends.friend_id == friend_id)
        )
        if friend_exists is not None:
            return {
                "message": "User is already a friend",
                "status_code": status.HTTP_409_CONFLICT,
            }

        await db.execute(
            insert(FriendRequests).values(user_id=user_id, friend_id=friend_id)
        )
        return {
            "message": "Friend request sent",
            "status_code": status.HTTP_201_CREATED,
        }

    @classmethod
    async def check_exsisting_request(self, user_id, friend_id):
        existing_request = await db.fetch_one(
            select([FriendRequests])
            .where(FriendRequests.user_id == user_id)
            .where(FriendRequests.friend_id == friend_id)
        )
        if existing_request is not None:
            return {
                "message": "You have already sent this user a friend request",
                "status_code": status.HTTP_400_BAD_REQUEST,
            }
        return None

    @classmethod
    async def get_friends(cls, user):
        friends = await db.fetch_all(
            select([Friends]).where(Friends.user_id == user.id)
        )
        friends = await db.fetch_all(
            select([User]).where(User.id.in_(friend["friend_id"] for friend in friends))
        )
        return {
            "message": "Your Friends",
            "data": [UserResponse(**friend) for friend in friends],
            "status_code": status.HTTP_200_OK,
        }

    @classmethod
    async def get_friend_requests(cls, user):
        approvals = await db.fetch_all(
            select([FriendRequests]).where(FriendRequests.friend_id == user.id)
        )
        approvals = await db.fetch_all(
            select([User]).where(
                User.id.in_(approval["user_id"] for approval in approvals)
            )
        )
        return {
            "message": "Friend requests",
            "data": [UserResponse(**approval) for approval in approvals],
            "status_code": status.HTTP_200_OK,
        }

    @classmethod
    async def get_exsisting_friend(cls, user, friend_id):
        friend = await db.fetch_one(
            select([Friends])
            .where(Friends.user_id == user.id)
            .where(Friends.friend_id == friend_id)
        )
        if friend is None:
            return {
                "message": "Friend not found",
                "status_code": status.HTTP_404_NOT_FOUND,
            }
        return None

    @classmethod
    async def accept_friend_request(cls, user, id):
        valid_user = await cls.get_user_by_id(id)
        if valid_user["status_code"] == status.HTTP_404_NOT_FOUND:
            return valid_user
        exsisting_friends = await cls.get_exsisting_friend(user, id)
        if exsisting_friends is None:
            return {
                "message": "User already added",
                "status_code": status.HTTP_409_CONFLICT,
            }
        check_exsisting_request = await UserService.check_exsisting_request(id, user.id)
        if check_exsisting_request is None:
            return {
                "message": "No friend request found",
                "status_code": status.HTTP_404_NOT_FOUND,
            }
        await db.execute(
            delete(FriendRequests)
            .where(FriendRequests.user_id == id)
            .where(FriendRequests.friend_id == user.id)
        )
        await db.execute(insert(Friends).values(user_id=user.id, friend_id=id))
        await db.execute(insert(Friends).values(friend_id=user.id, user_id=id))
        return {"message": "Friend request accepted", "status_code": status.HTTP_200_OK}

    @classmethod
    async def reject_friend_request(cls, user, id):
        valid_user = await cls.get_user_by_id(id)
        if valid_user["status_code"] == status.HTTP_404_NOT_FOUND:
            return valid_user
        check_exsisting_request = await UserService.check_exsisting_request(id, user.id)
        if check_exsisting_request is None:
            return {
                "message": "No friend request found",
                "status_code": status.HTTP_404_NOT_FOUND,
            }
        await db.execute(
            delete(FriendRequests)
            .where(FriendRequests.user_id == id)
            .where(FriendRequests.friend_id == user.id)
        )
        return {"message": "Friend request rejected", "status_code": status.HTTP_200_OK}

    @classmethod
    async def delete_friendrequest(cls, user, id):
        valid_user = await cls.get_user_by_id(id)
        if valid_user["status_code"] == status.HTTP_404_NOT_FOUND:
            return valid_user
        check_exsisting_request = await UserService.check_exsisting_request(user.id, id)
        if check_exsisting_request is None:
            return {
                "message": "No friend request found",
                "status_code": status.HTTP_404_NOT_FOUND,
            }
        await db.execute(
            delete(FriendRequests)
            .where(FriendRequests.user_id == user.id)
            .where(FriendRequests.friend_id == id)
        )
        return {"message": "Friend request deleted", "status_code": status.HTTP_200_OK}

    @classmethod
    async def remove_friend(cls, user, id):
        valid_user = await cls.get_user_by_id(id)
        if valid_user["status_code"] == status.HTTP_404_NOT_FOUND:
            return valid_user
        existing_friend = await db.fetch_one(
            select([Friends])
            .where(Friends.user_id == user.id)
            .where(Friends.friend_id == id)
        )
        if existing_friend is None:
            return {
                "message": "Friend not found",
                "status_code": status.HTTP_404_NOT_FOUND,
            }
        await db.execute(
            delete(Friends)
            .where(Friends.user_id == user.id)
            .where(Friends.friend_id == id)
        )
        await db.execute(
            delete(Friends)
            .where(Friends.user_id == id)
            .where(Friends.friend_id == user.id)
        )
        return {"message": "Friend deleted", "status_code": status.HTTP_200_OK}
