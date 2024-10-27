from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    interactions = relationship("UserInteraction", back_populates="user", cascade="all, delete-orphan")
