from fastapi import APIRouter
from app.schemas import UserLoginRequest,UserSignInRequest
from app.services import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(request: UserLoginRequest):
    return AuthService.login(request)
@router.post("/signup")
async def signup(request: UserSignInRequest):
    return AuthService.signup(request)
