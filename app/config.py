import os
from dotenv import load_dotenv

load_dotenv()

class config:
    LOCAL_POSTGRES_USER = os.environ.get("LOCAL_POSTGRES_USER")
    LOCAL_POSTGRES_PASSWORD = os.environ.get("LOCAL_POSTGRES_PASSWORD")
    LOCAL_POSTGRES_DATABASE = os.environ.get("LOCAL_POSTGRES_DATABASE")
    LOCAL_POSTGRES_SERVER = os.environ.get("LOCAL_POSTGRES_SERVER")
    
    REMOTE_POSTGRES_USER = os.environ.get("REMOTE_POSTGRES_USER")
    REMOTE_POSTGRES_PASSWORD = os.environ.get("REMOTE_POSTGRES_PASSWORD")
    REMOTE_POSTGRES_DATABASE = os.environ.get("REMOTE_POSTGRES_DATABASE")
    REMOTE_POSTGRES_SERVER = os.environ.get("REMOTE_POSTGRES_SERVER")
    DATABASE_TYPE = os.environ.get("DATABASE_TYPE")
    
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = os.environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")