from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.users.auth import create_access_token, verify_password
from app.config import settings
from jose import JWTError, jwt

from app.users.schema import UserResponse, UserCreate, Token
from app.users.controller import create_user, get_user, get_user_by_name
from app.exceptions import IncorrectEmailOrPassword, UserAlreadyExistsException
from app.users.auth import oauth2_scheme

router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    user_exists = get_user_by_name(db, user.username)
    if user_exists:
        raise UserAlreadyExistsException
    return create_user(db, user)

@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_name(db, user.username)

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=UserResponse)
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