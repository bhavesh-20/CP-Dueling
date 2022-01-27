import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE")
    POSTGRES_SERVER = os.environ.get("POSTGRES_SERVER")