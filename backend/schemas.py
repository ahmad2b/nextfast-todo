from pydantic import BaseModel


class TodoRequest(BaseModel):
    title: str
    description: str
    completed: bool = False


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True
