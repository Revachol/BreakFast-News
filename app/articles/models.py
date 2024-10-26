from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from app.database import Base
from datetime import datetime

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
    site = Column(Integer, ForeignKey("sites.smi_id"), nullable=False)
    tags = Column(ARRAY(Integer), nullable=True)  # Массив id тегов

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    interests = Column(ARRAY(Integer), nullable=True)  # Массив id тегов

class UserInteraction(Base):
    __tablename__ = 'user_interactions'

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"), primary_key=True)
    like = Column(Boolean, nullable=False)  # True — лайк, False — дизлайк
    timestamp = Column(DateTime, default=datetime.utcnow)

class Tag(Base):
    __tablename__ = 'tags'

    tag_id = Column(Integer, primary_key=True)
    tag = Column(String, unique=True, nullable=False)  # Название тега

class Site(Base):
    __tablename__ = 'sites'

    smi_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)  # Название СМИ
