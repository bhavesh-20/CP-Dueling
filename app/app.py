from fastapi import FastAPI

from app.database import Base, SessionLocal, db, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
async def connect():
    await db.connect()


@app.on_event("shutdown")
async def disconnect():
    await db.disconnect()
