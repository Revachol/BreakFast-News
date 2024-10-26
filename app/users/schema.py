"""
Схемы используются для валидации данных при передаче их между контроллерами и представлениями.
"""

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
