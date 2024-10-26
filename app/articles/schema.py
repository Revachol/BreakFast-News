from pydantic import BaseModel
from typing import Dict, Any


class ArticleBase(BaseModel):
    title: str
    link: str
    key_words: Dict[str, Any]


class ArticleCreate(ArticleBase):
    pass


class ArticleResponce(ArticleBase):
    id: int

    class Config:
        orm_mode = True
