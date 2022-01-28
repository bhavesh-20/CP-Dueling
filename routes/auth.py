from fastapi import APIRouter
from services import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])
