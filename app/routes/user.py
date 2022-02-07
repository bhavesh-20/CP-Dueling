from fastapi import APIRouter, Depends, Response, status

from app.schemas import UserResponse
from app.services import UserService
from app.utils import authenticate_user

router = APIRouter(prefix="/user", tags=["user_module"])


@router.get("/:id")
async def get_user_by_id(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    user = await UserService.get_user_by_id(id)
    response.status_code = user["status_code"]
    return user


@router.get("/:name")
async def get_user_by_name(
    name: str, response: Response, user: UserResponse = Depends(authenticate_user)
):
    user = await UserService.get_user_by_name(name)
    Response.status_code = user["status_code"]
    return user


@router.post("/friend/:id")
async def add_friend(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    user = await UserService.add_friend(id, user)
    response.status_code = user["status_code"]
    return user


@router.get("/friends")
async def get_friends(
    response: Response, user: UserResponse = Depends(authenticate_user)
):
    user = await UserService.get_friends(user)
    response.status_code = user["status_code"]
    return user
