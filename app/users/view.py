# app/views/user_view.py
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.users.auth import create_access_token, verify_password
from app.config import settings

from jose import JWTError, jwt  # Импортируем jwt из jose

from app.users.schema import UserResponse, UserCreate
from app.users.controller import create_user, get_user, get_user_by_name
from app.exceptions import IncorrectEmailOrPassword, UserAlreadyExistsException

router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    user_exists = get_user_by_name(db, user.username)
    if user_exists:
        raise UserAlreadyExistsException
    return create_user(db, user)


"""
@router.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user(db, username=username)
    if user is None:
        raise credentials_exception
    return user
"""
