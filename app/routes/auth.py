from fastapi import APIRouter, Depends, Response, status

from app import db
from app.schemas import UserLoginRequest, UserResponse, UserSignupRequest
from app.services import AuthService
from app.utils import authenticate_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(request: UserLoginRequest, response: Response):
    """End point for the registed users to login."""
    async with db.transaction():
        resp = await AuthService.login(request)
        response.status_code = resp["status_code"]
        return resp


@router.post("/signup")
async def signup(request: UserSignupRequest, response: Response):
    """End point for new users to register for the first time."""
    async with db.transaction():
        resp = await AuthService.signup(request)
        response.status_code = resp["status_code"]
        return resp


@router.get("/jwt")
async def jwt(user: UserResponse = Depends(authenticate_user)):
    """End point to get the details of the logged in user."""
    async with db.transaction():
        return {"message": "Success", "data": user, "status_code": status.HTTP_200_OK}
