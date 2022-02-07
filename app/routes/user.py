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
async def send_friend_request(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    user = await UserService.send_friend_request(id, user)
    response.status_code = user["status_code"]
    return user


@router.get("/friends")
async def get_friends(
    response: Response, user: UserResponse = Depends(authenticate_user)
):
    user = await UserService.get_friends(user)
    response.status_code = user["status_code"]
    return user


@router.get("/freindsrequests")
async def get_friend_requests(
    response: Response, user: UserResponse = Depends(authenticate_user)
):
    user = await UserService.get_friend_requests(user)
    response.status_code = user["status_code"]
    return user


@router.post("/acceptfriendrequest/:id")
async def accept_friend_request(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    user = await UserService.accept_friend_request(user, id)
    response.status_code = user["status_code"]
    return user


@router.post("/rejectfriendrequest/:id")
async def reject_friend_request(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    user = await UserService.reject_friend_request(user, id)
    response.status_code = user["status_code"]
    return user
