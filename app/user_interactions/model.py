from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class UserInteraction(Base):
    __tablename__ = "user_interactions"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"), primary_key=True)
    redirect = Column(Boolean, default=False)

    # user = relationship("User", back_populates="interactions")
    # article = relationship("Article", back_populates="interactions")