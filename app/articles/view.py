# app/views/user_view.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.articles.schema import ArticleCreate, ArticleResponce
from app.articles import controller

router = APIRouter()


@router.post("/article/", response_model=ArticleResponce)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    return controller.create_article(db=db, article=article)


@router.get("/article/{article_id}", response_model=ArticleResponce)
def read_article(article_id: int, db: Session = Depends(get_db)):
    db_article = controller.get_article(db, article_id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article


@router.get("/articles/", response_model=list[ArticleResponce])
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return controller.get_article(db, skip=skip, limit=limit)
