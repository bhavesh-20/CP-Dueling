from fastapi import status
from passlib.context import CryptContext
from sqlalchemy.sql.expression import insert, select

from app import db
from app.models import User
from app.schemas import UserLoginRequest, UserSignupRequest
from app.utils import JWTtoken


class AuthService:

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    async def login(cls, request: UserLoginRequest):
        """Functionality for /login endpoint. And also JWT token creation invoked."""
        user = await db.fetch_one(select([User]).where(User.email == request.email))

        if user is None:
            return {
                "message": "User not found",
                "status_code": status.HTTP_404_NOT_FOUND,
            }
        if not cls.pwd_context.verify(request.password, user.hashed_password):
            return {
                "message": "Invalid password",
                "status_code": status.HTTP_401_UNAUTHORIZED,
            }

        op_status, data = await JWTtoken.create_access_token(
            {"username": user.username}
        )
        if not op_status:
            return {"message": data["message"], "status_code": data["status_code"]}
        return {
            "message": "Login Successful",
            "access_token": data["access_token"],
            "status_code": status.HTTP_200_OK,
        }

    @classmethod
    async def signup(cls, request: UserSignupRequest):
        """Functionality for /signup endpoint.(New User)"""
        user = await db.fetch_one(select([User]).where(User.email == request.email))
        if user is not None:
            return {
                "message": "User already exists",
                "status_code": status.HTTP_409_CONFLICT,
            }
        await db.execute(
            insert(User).values(
                email=request.email,
                username=request.username,
                hashed_password=cls.pwd_context.hash(request.password),
            )
        )
        return {"message": "Signup Successful", "status_code": status.HTTP_201_CREATED}
