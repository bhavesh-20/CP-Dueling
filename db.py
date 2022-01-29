from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import config
import urllib

if config.DATABASE_TYPE == "local":
    SQLALCHEMY_DATABASE_URL = f"postgresql://{config.LOCAL_POSTGRES_USER}:{urllib.parse.quote_plus(config.LOCAL_POSTGRES_PASSWORD)}@{config.LOCAL_POSTGRES_SERVER}/{config.LOCAL_POSTGRES_DATABASE}"
else:
    SQLALCHEMY_DATABASE_URL = f"postgresql://{config.REMOTE_POSTGRES_USER}:{urllib.parse.quote_plus(config.REMOTE_POSTGRES_PASSWORD)}@{config.REMOTE_POSTGRES_SERVER}/{config.REMOTE_POSTGRES_DATABASE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()