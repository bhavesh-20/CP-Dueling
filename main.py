from fastapi import FastAPI
from db import SessionLocal, engine
from routes import auth_router
import models

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello Dev!"}

app.include_router(auth_router)