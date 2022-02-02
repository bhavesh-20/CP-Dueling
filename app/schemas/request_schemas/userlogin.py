from pydantic import BaseModel

class UserLoginRequest(BaseModel):
    email: str
    password: str

class UserSignInRequest(BaseModel):
    username: str
    email: str
    password: str