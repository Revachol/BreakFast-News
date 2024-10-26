from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from . import model, schema
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=List[schema.Article])
def get_articles(tag: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(model.Article)
    if tag:
        query = query.filter(model.Article.tags.any(tag))
    articles = query.all()
    return articles
