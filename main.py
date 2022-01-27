from fastapi import FastAPI
from db import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Dev!"}