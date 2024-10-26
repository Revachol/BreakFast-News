from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from app.database import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
    site = Column(Integer, ForeignKey("sites.smi_id"), nullable=False)
    tags = Column(ARRAY(Integer), nullable=True)  # Массив id тегов
