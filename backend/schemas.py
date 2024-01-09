from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TodoRequest(BaseModel):
    title: str
    description: str
    completed: bool = False


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class ConfigDict:
        orm_mode = True


class TokenData(BaseModel):
    sub: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    password: str
    todos: List[TodoResponse] = []
    created_at: datetime

    class ConfigDict:
        orm_mode = True
