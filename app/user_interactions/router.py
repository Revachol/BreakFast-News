from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from . import model, schema
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schema.UserInteraction)
def like_dislike_article(interaction: schema.UserInteractionCreate, db: Session = Depends(get_db)):
    new_interaction = model.UserInteraction(**interaction.dict())
    db.add(new_interaction)
    db.commit()
    db.refresh(new_interaction)
    return new_interaction

@router.get("/feed/{user_id}", response_model=List[schema.Article])
def get_user_feed(user_id: int, db: Session = Depends(get_db)):
    user_interactions = db.query(model.UserInteraction).filter(model.UserInteraction.user_id == user_id).all()
    article_ids = [interaction.article_id for interaction in user_interactions]
    articles = db.query(model.Article).filter(model.Article.id.in_(article_ids)).all()
    return articles