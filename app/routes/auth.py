from fastapi import APIRouter, Depends, Response, status

from app.schemas import UserLoginRequest, UserResponse, UserSignupRequest
from app.services import AuthService
from app.utils import authenticate_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(request: UserLoginRequest, response: Response):
    resp = await AuthService.login(request)
    response.status_code = resp["status_code"]
    return resp


@router.post("/signup")
async def signup(request: UserSignupRequest, response: Response):
    resp = await AuthService.signup(request)
    response.status_code = resp["status_code"]
    return resp


@router.get("/jwt")
async def jwt(user: UserResponse = Depends(authenticate_user)):
    return {"message": "Success", "data": user, "status_code": status.HTTP_200_OK}
