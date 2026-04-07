from fastapi import FastAPI
from backend.core.config import settings
from backend.db.session import engine
from backend.db.models.user import User
from backend.db.models.blog import Blog
from backend.db.base_class import Base

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    # create_tables() -- Tab;es shouldn't be created this way
    return app

app = start_application()

@app.get("/")
def hello():
    return {
        "msg": "Hello FastAPI"
    }