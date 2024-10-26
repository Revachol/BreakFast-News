from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Tag])
def get_tags(db: Session = Depends(get_db)):
    tags = db.query(models.Tag).all()
    return tags

@router.post("/", response_model=schemas.Tag)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    new_tag = models.Tag(**tag.dict())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag
