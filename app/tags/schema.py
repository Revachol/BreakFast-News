from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Схемы для таблицы `articles`
class ArticleBase(BaseModel):
    title: str
    link: str
    site: int
    tags: List[int] = []

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True

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

# Схемы для таблицы `tags`
class TagBase(BaseModel):
    tag: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    tag_id: int

    class Config:
        orm_mode = True

# Схемы для таблицы `sites`
class SiteBase(BaseModel):
    name: str

class SiteCreate(SiteBase):
    pass

class Site(SiteBase):
    smi_id: int

    class Config:
        orm_mode = True
