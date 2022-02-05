import urllib

import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import config

ssl_connection = False
if config.DATABASE_TYPE == "local":
    SQLALCHEMY_DATABASE_URI = f"postgresql://{config.LOCAL_POSTGRES_USER}:{urllib.parse.quote_plus(config.LOCAL_POSTGRES_PASSWORD)}@{config.LOCAL_POSTGRES_SERVER}/{config.LOCAL_POSTGRES_DATABASE}"
else:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{config.REMOTE_POSTGRES_USER}:{urllib.parse.quote_plus(config.REMOTE_POSTGRES_PASSWORD)}@{config.REMOTE_POSTGRES_SERVER}/{config.REMOTE_POSTGRES_DATABASE}"
    ssl_connection = True

engine = create_engine(SQLALCHEMY_DATABASE_URI)
db = databases.Database(SQLALCHEMY_DATABASE_URI, ssl=ssl_connection, min_size=1)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
