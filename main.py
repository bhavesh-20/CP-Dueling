from app import app
from app.routes import auth_router

@app.get("/")
async def home():
    return {"message": "Hello Dev!"}

app.include_router(auth_router)