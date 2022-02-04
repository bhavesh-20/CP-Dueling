from fastapi import APIRouter, Response

from app.schemas import UserLoginRequest, UserSignupRequest
from app.services import AuthService

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
