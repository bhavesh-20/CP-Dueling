from jose import JWTError, jwt
from typing import Optional
from datetime import datetime, timedelta 
from app.config import config
from fastapi import status


class JWTtoken:
    
    @classmethod
    async def create_access_token(cls, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=int(config.ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
        return (True,{"access_token": encoded_jwt})

    @classmethod
    async def decode_access_token(cls, access_token: str):
        try:
            payload = jwt.decode(access_token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
            return (True,{"data": payload})
        except JWTError:
            return (False,{"message": "Invalid token", "status_code": status.HTTP_401_UNAUTHORIZED})
