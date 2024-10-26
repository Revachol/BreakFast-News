from sqlalchemy import Column, Integer, String, JSON
from app.database import Base
from sqlalchemy.dialects.postgresql import ARRAY


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
    key_words = Column(JSON)  # Массив id тегов
