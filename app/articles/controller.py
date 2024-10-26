"""
Контроллер будет содержать логику для работы с базой данных.
"""

from sqlalchemy.orm import Session
from app.articles.model import Article
from app.articles.schema import ArticleCreate


def create_article(db: Session, article: ArticleCreate):
    db_article = Article(
        title=article.title, link=article.link, key_words=article.key_words
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_article(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()


def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Article).offset(skip).limit(limit).all()
