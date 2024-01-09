from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from db import SessionLocal, get_db
import schemas, crud, auth, models, config
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()


@router.post(
    "/signup",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, username=user.username)

    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@router.post("/login", response_model=schemas.Token)
def login(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    """
    Login route. Returns a JWT token to be used in subsequent requests.
    """
    db_user = crud.get_user(db, username=user.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=30)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=schemas.UserResponse)
async def read_users_me(
    current_user: schemas.UserResponse = Depends(auth.get_current_user),
):
    """
    Get the login user information.
    """
    return current_user
