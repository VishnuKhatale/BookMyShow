from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    first_name : str
    last_name : str
    email : str
    phone_number : str
    user_type : str
    is_deleted: Optional[bool] = False

class UserResponse(User):
    user_id : int


class UserCreate(User):
    created_at : datetime
    updated_at : datetime
    password : str

class UserUpdate(User):
    updated_at : datetime
    password : str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user: User