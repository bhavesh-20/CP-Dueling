from datetime import datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.sql.expression import select

from app import db
from app.models import User
from app.schemas import UserResponse

from .JWTtoken import JWTtoken

security = HTTPBearer()

"""The generated JWT Token is validated."""


async def authenticate_user(authorization=Depends(security)):
    access_token = authorization.credentials
    if access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Access Token not provided"
        )
    op_status, resp = await JWTtoken.decode_access_token(access_token)
    if not op_status:
        raise HTTPException(status_code=resp["status_code"], detail=resp["message"])

    expiry_date = datetime.fromtimestamp(resp["data"]["exp"])
    if expiry_date < datetime.now():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired"
        )

    data = resp["data"]["data"]
    user = await db.fetch_one(select(User).where(User.username == data["username"]))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )

    return UserResponse(**user)
