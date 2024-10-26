from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.database import Base


class Tag(Base):
    __tablename__ = 'tags'

    tag_id = Column(Integer, primary_key=True)
    tag = Column(String, unique=True, nullable=False)  # Название тега
