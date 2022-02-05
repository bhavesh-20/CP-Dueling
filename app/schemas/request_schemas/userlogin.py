from pydantic import BaseModel


class UserLoginRequest(BaseModel):
    email: str
    password: str


class UserSignupRequest(BaseModel):
    username: str
    email: str
    password: str
