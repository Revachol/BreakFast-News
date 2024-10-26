from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    interests = Column(ARRAY(Integer), nullable=True)  # Массив id тегов
