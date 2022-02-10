from fastapi import APIRouter, Depends, Response, status

from app import db
from app.schemas import UserResponse
from app.services import FriendService, UserService
from app.utils import authenticate_user

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/:id")
async def get_user_by_id(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    async with db.transaction():
        resp = await UserService.get_user_by_id(id)
        response.status_code = resp["status_code"]
        return resp


@router.get("/:username")
async def get_user_by_username(
    username: str, response: Response, user: UserResponse = Depends(authenticate_user)
):
    async with db.transaction():
        resp = await UserService.get_user_by_name(username)
        response.status_code = resp["status_code"]
        return resp


@router.post("/friend/:id")
async def send_friend_request(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    async with db.transaction():
        resp = await FriendService.send_friend_request(id, user)
        response.status_code = resp["status_code"]
        return resp


@router.get("/friends")
async def get_friends(
    response: Response, user: UserResponse = Depends(authenticate_user)
):
    async with db.transaction():
        resp = await FriendService.get_friends(user)
        response.status_code = resp["status_code"]
        return resp


@router.get("/freindsrequests")
async def get_friend_requests(
    response: Response, user: UserResponse = Depends(authenticate_user)
):
    async with db.transaction():
        resp = await FriendService.get_friend_requests(user)
        response.status_code = resp["status_code"]
        return resp


@router.post("/acceptfriendrequest/:id")
async def accept_friend_request(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    async with db.transaction():
        resp = await FriendService.accept_friend_request(user, id)
        response.status_code = resp["status_code"]
        return resp


@router.post("/rejectfriendrequest/:id")
async def reject_friend_request(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    async with db.transaction():
        resp = await FriendService.reject_friend_request(user, id)
        response.status_code = resp["status_code"]
        return resp


@router.post("/removefriend/:id")
async def remove_friend(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    async with db.transaction():
        resp = await FriendService.remove_friend(user, id)
        response.status_code = resp["status_code"]
        return resp


@router.post("/deletefriendrequest/:id")
async def delete_friend_request(
    id: int, response: Response, user: UserResponse = Depends(authenticate_user)
):
    async with db.transaction():
        resp = await FriendService.delete_friend_request(user, id)
        response.status_code = resp["status_code"]
        return resp
