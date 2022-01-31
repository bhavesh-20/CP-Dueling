from fastapi import FastAPI
from .db import SessionLocal, engine
from app.routes import auth_router
from app import models

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

app = FastAPI()