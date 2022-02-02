from app import db
from app.schemas import UserLoginRequest,UserSignInRequest
from app.models import User
import jwt
from passlib.context import CryptContext
class AuthService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    @classmethod
    def login(cls,request: UserLoginRequest):
         user = db.query(User).filter(User.email == request.email).first()
         if user is None:
           return {"message": "User not found"}
         if not cls.pwd_context.verify(request.password, user.hashed_password):
            return {"message": "Invalid password"}
        
         return {"message": "Login Successful", "token": jwt.encode({"username": user.username, "email": user.email}, "secret")}

    @classmethod
    def signup(cls,request: UserSignInRequest):
        user = db.query(User).filter(User.email == request.email).first()
        if user is not None:
            return {"message": "User already exists"}
        new_user=User(username=request.username,email=request.email,hashed_password=cls.pwd_context.hash(request.password))
        db.add(new_user)
        db.commit()
        return {"message": new_user.hashed_password}