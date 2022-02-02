from fastapi import FastAPI
from .database import SessionLocal, engine
from app.database import Base

Base.metadata.create_all(bind=engine)

db = SessionLocal()

app = FastAPI()