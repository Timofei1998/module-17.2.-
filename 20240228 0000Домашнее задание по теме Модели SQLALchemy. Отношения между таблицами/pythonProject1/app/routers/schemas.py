from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    content: str
    priority: int = 0
    completed: bool = False
    user_id: int

class UserBase(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
