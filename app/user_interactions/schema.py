from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# Схемы для таблицы `user_interactions`
class UserInteractionBase(BaseModel):
    user_id: int
    article_id: int
    like: bool
    timestamp: Optional[datetime] = None

class UserInteractionCreate(UserInteractionBase):
    pass

class UserInteraction(UserInteractionBase):
    class Config:
        orm_mode = True
