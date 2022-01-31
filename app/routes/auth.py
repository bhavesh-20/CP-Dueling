from fastapi import APIRouter
from app.services import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])
