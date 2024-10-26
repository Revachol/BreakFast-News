from pydantic import BaseModel
from typing import List


# Схемы для таблицы `users`
class UserBase(BaseModel):
    username: str
    interests: List[int] = []

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
