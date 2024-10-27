from pydantic import BaseModel
from typing import Dict, Any, Optional


class ArticleBase(BaseModel):
    title: str
    link: str


# key_words: Dict[str, Any]


class ArticleCreate(ArticleBase):
    key_words: Dict[str, Any]
    pass


class ArticleResponce(ArticleBase):
    id: int

    class Config:
        orm_mode = True
        # exclude = {"key_words"}
