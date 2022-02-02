from pydantic import BaseModel

class UserLoginRequest(BaseModel):
    email: str
    password: str