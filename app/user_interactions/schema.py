from pydantic import BaseModel

class UserInteractionBase(BaseModel):
    user_id: int
    article_id: int

class UserInteractionCreate(UserInteractionBase):
    redirect: bool = False

class UserInteractionUpdate(UserInteractionBase):
    redirect: bool
