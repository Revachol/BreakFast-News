from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import model, schema
from ..database import get_db

router = APIRouter()

# @router.post("/register", response_model=schema.User)
# def register_user(user: schema.UserCreate, db: Session = Depends(get_db)):
#     db_user = db.query(model.User).filter(model.User.username == user.username).first()
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already registered")
#     new_user = model.User(username=user.username, interests=user.interests)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#
# @router.get("/{user_id}", response_model=schema.User)
# def get_user_profile(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(model.User).filter(model.User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
