# app/views/user_view.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.articles.schema import ArticleCreate, ArticleResponce
from app.articles import controller

from app.recommendation.recommendation import get_recommendations
from app.articles.model import Article


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



@router.get("/")
def read_root(user_id: int = 1, db: Session = Depends(get_db)):
    get_recommendations(db, 0, 6, user_id)
    return {"message": "Hello, World!"}

@router.get("/posts")
def get_posts_in_range(left: int, right: int, db: Session = Depends(get_db)):
    # Проверяем, что границы корректные
    if left < 0 or right < 0 or left > right:
        raise HTTPException(status_code=400, detail="Invalid range")

    # Запрашиваем статьи из базы данных в заданном диапазоне
    posts = db.query(Article.id).filter(Article.id >= left, Article.id <= right).all()

    # Преобразуем результаты в список идентификаторов
    post_ids = [post.id for post in posts]

    return post_ids

