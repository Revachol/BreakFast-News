from sqlalchemy.orm import Session
from app.user_interactions.model import UserInteraction
from app.user_interactions.schema import UserInteractionCreate, UserInteractionUpdate


def create_user_interaction(db: Session, interaction: UserInteractionCreate):
    db_interaction = UserInteraction(
        user_id=interaction.user_id,
        article_id=interaction.article_id,
        redirect=interaction.redirect,
    )
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction


def update_redirect(db: Session, interaction_update: UserInteractionUpdate):
    db_interaction = (
        db.query(UserInteraction)
        .filter(
            UserInteraction.user_id == interaction_update.user_id,
            UserInteraction.article_id == interaction_update.article_id,
        )
        .first()
    )

    if db_interaction:
        db_interaction.redirect = interaction_update.redirect
        db.commit()
        db.refresh(db_interaction)
    return db_interaction


def get_user_interactions(db: Session, user_id: int):
    # Запрос всех взаимодействий для указанного пользователя
    interactions = (
        db.query(UserInteraction).filter(UserInteraction.user_id == user_id).all()
    )
    return interactions
