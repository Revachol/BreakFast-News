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
