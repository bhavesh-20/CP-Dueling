from fastapi import APIRouter, Depends, Response, status

from app.schemas import UserResponse
from app.services import UserService
from app.utils import authenticate_user

router = APIRouter(prefix="/user", tags=["user_module"])


@router.get("/:id")
async def get_user_by_id(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    resp = await UserService.get_user_by_id(id)
    response.status_code = resp["status_code"]
    return resp


@router.get("/:username")
async def get_user_by_username(
    username: str, response: Response, user: UserResponse = Depends(authenticate_user)
):
    resp = await UserService.get_user_by_name(username)
    response.status_code = resp["status_code"]
    return resp


@router.post("/friend/:id")
async def send_friend_request(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    resp = await UserService.send_friend_request(id, user)
    response.status_code = resp["status_code"]
    return resp


@router.get("/friends")
async def get_friends(
    response: Response, user: UserResponse = Depends(authenticate_user)
):
    resp = await UserService.get_friends(user)
    response.status_code = resp["status_code"]
    return resp


@router.get("/freindsrequests")
async def get_friend_requests(
    response: Response, user: UserResponse = Depends(authenticate_user)
):
    resp = await UserService.get_friend_requests(user)
    response.status_code = resp["status_code"]
    return resp


@router.post("/acceptfriendrequest/:id")
async def accept_friend_request(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    resp = await UserService.accept_friend_request(user, id)
    response.status_code = resp["status_code"]
    return resp


@router.post("/rejectfriendrequest/:id")
async def reject_friend_request(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    resp = await UserService.reject_friend_request(user, id)
    response.status_code = resp["status_code"]
    return resp


@router.post("/removefriend/:id")
async def remove_friend(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    resp = await UserService.remove_friend(user, id)
    response.status_code = resp["status_code"]
    return resp


@router.post("/deletefriendrequest/:id")
async def delete_friend_request(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    resp = await UserService.delete_friendrequest(user, id)
    response.status_code = resp["status_code"]
    return resp
