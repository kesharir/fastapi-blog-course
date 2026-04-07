from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print(f" DatabaseUrl is : {SQLALCHEMY_DATABASE_URL}")
# Entry point for any sqlalchemy application
engine=create_engine(SQLALCHEMY_DATABASE_URL)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SESSIONLOCAL=sessionmaker(autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SESSIONLOCAL()
        yield db
    finally:
        db.close()