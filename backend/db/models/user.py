from backend.db.base import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from backend.db.models.blog import Blog

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    blogs = relationship("Blog", back_populates="author")