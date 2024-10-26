from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.database import Base
from datetime import datetime


class UserInteraction(Base):
    __tablename__ = 'user_interactions'

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"), primary_key=True)
    like = Column(Boolean, nullable=False)  # True — лайк, False — дизлайк
    timestamp = Column(DateTime, default=datetime.utcnow)
