from fastapi import FastAPI

from backend.apis.base import api_router
from backend.core.config import settings
from backend.db.session import engine
from backend.db.base_class import Base

def include_router(app):
    app.include_router(api_router)

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    # create_tables() -- Tables shouldn't be created this way
    return app

app = start_application()

@app.get("/")
def hello():
    return {
        "msg": "Hello FastAPI"
    }