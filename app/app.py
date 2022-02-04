from fastapi import FastAPI

from app.database import Base, database

from .database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

db = SessionLocal()

app = FastAPI()


@app.on_event("startup")
async def connect():
    await database.connect()


@app.on_event("shutdown")
async def disconnect():
    await database.disconnect()
