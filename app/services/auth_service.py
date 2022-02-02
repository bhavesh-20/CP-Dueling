from app import db
from app.schemas import UserLoginRequest,UserSignInRequest
from app.models import User
import jwt
class AuthService:

    @classmethod
    def login(cls,request: UserLoginRequest):
         user = db.query(User).filter(User.email == request.email).first()
         if user is None:
           return {"message": "User not found"}
         if user.hashed_password != request.password:
            return {"message": "Invalid password"}
        
         return {"message": "Login Successful", "token": jwt.encode({"username": user.username, "email": user.email}, "secret")}

    @classmethod
    def signup(cls,request: UserSignInRequest):
        user = db.query(User).filter(User.email == request.email).first()
        if user is not None:
            return {"message": "User already exists"}
        new_user=User(username=request.username,email=request.email,hashed_password=request.password)
        db.add(new_user)
        db.commit()
        return {"message": "User created"}