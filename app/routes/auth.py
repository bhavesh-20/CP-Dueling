from fastapi import APIRouter
from app.schemas import UserLoginRequest,UserSignupRequest
from app.services import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(request: UserLoginRequest):
    return await AuthService.login(request)
@router.post("/signup")
async def signup(request: UserSignupRequest):
    return await AuthService.signup(request)
