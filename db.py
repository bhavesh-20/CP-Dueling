from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config
import urllib

SQLALCHEMY_DATABASE_URL = f"postgresql://{Config.POSTGRES_USER}:{urllib.parse.quote_plus(Config.POSTGRES_PASSWORD)}@{Config.POSTGRES_SERVER}/{Config.POSTGRES_DATABASE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()