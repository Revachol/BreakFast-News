from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.database import Base

class Site(Base):
    __tablename__ = 'sites'

    smi_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)  # Название СМИ
