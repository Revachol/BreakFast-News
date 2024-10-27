"""
Контроллер будет содержать логику для работы с базой данных.
"""

from sqlalchemy.orm import Session
from app.articles.model import Article
from app.articles.schema import ArticleCreate
from app.user_interactions.model import UserInteraction
from sqlalchemy import desc


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


def get_articles(db: Session, skip: int = 0):
    return db.query(Article).offset(skip).all()


def get_articles_with_interactions(db: Session):
    # Получение всех статей, у которых есть взаимодействия, и сортировка по убыванию
    articles = (
        db.query(Article)
        .join(UserInteraction)
        .group_by(Article.id)  # Группируем по id статьи
        .order_by(desc(Article.id))  # Сортировка по убыванию
        .all()
    )
    return articles


def get_articles_for_user(db: Session, user_id: int):
    # Получение всех статей для указанного пользователя
    articles = (
        db.query(Article)
        .join(UserInteraction, Article.id == UserInteraction.article_id)
        .filter(UserInteraction.user_id == user_id)
        .all()
    )
    return articles


"""


def get_articles_for_user(db: Session, user_id: int):
    # Запрос, который возвращает статьи и булево поле из UserInteraction для указанного пользователя
    results = (
        db.query(Article, UserInteraction.redirect)
        .join(UserInteraction, Article.id == UserInteraction.article_id)
        .filter(UserInteraction.user_id == user_id)
        .all()
    )
    return results
"""
