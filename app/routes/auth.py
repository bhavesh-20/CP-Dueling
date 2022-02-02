from fastapi import APIRouter, Depends
from app.schemas import UserLoginRequest
from app.models import User
from app import db
import jwt

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(request: UserLoginRequest):
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        return {"message": "User not found"}
    if user.hashed_password != request.password:
        return {"message": "Invalid password"}
    
    return {"message": "Login Successful", "token": jwt.encode({"username": user.username, "email": user.email}, "secret")}