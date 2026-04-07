import time
from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, Field, validator, root_validator
# Custom Validators:
# - Phone number to start with some digits
# Meaningful errors

class Language(str, Enum):
    PY = "python"
    JAVA = "java"
    GO = "go"

class Comment(BaseModel):
    text: Optional[str] = None

class Blog(BaseModel):
    # title: str = Field(min_length=10)
    title: str
    description: Optional[str] = None
    is_active: bool
    language: Language = Language.JAVA
    created_at: datetime = Field(default_factory = datetime.now)
    comments: Optional[List[Comment]] = None

first_blog = Blog(title="My title", is_active=True)
print(first_blog)

# time.sleep(10)

second_blog = Blog(title="My title", is_active=True, comments=[Comment(text="My First Comment")])
print(second_blog)
# Pydantic throws Error
# is_active
#   Input should be a valid boolean, unable to interpret input [type=bool_parsing, input_value='ip', input_type=str]
# Blog(title="My title", is_active="ip")

"""
Custom Validation with Pydantic: 
"""

class CreateUser(BaseModel):
    email: str
    password: str
    confirm_password: str

    @validator("email")
    def validate_email(cls, value):
        if "admin" in value:
            raise ValueError("This email is not allowed")
        return value
    @root_validator()
    def validate_password(cls, values):
        password=values.get("password")
        confirm_password=values.get("confirm_password")

        if password != confirm_password:
            raise ValueError("password and confirm password don't match")

CreateUser(email="admin@xyz.com", password="123", confirm_password="1234")

