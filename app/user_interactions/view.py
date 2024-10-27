from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from app.user_interactions.controller import create_user_interaction, update_redirect
from app.user_interactions.schema import UserInteractionCreate, UserInteractionUpdate

router = APIRouter()

@router.post("/interactions/", response_model=UserInteractionCreate)
def like_article(interaction: UserInteractionCreate, db: Session = Depends(get_db)):
    db_interaction = create_user_interaction(db=db, interaction=interaction)
    return db_interaction

# @router.put("/interactions/redirect", response_model=UserInteractionUpdate)
# def set_redirect(interaction_update: UserInteractionUpdate, db: Session = Depends(get_db)):
#     db_interaction = update_redirect(db=db, interaction_update=interaction_update)
#     if not db_interaction:
#         raise HTTPException(status_code=404, detail="Interaction not found")
#     return db_interaction
