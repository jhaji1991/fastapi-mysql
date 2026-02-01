from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.user import User
from app.crud import user as crud_user
from app.utils.logger import logger

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/")
def create_user(user: User, db: Session = Depends(get_db)):
    logger.info(f"Creating user: {user.email}")
    return crud_user.create_user(db, user)

@router.get("/users/")
def read_users(db: Session = Depends(get_db)):
    logger.info("Fetching all users")
    return crud_user.get_users(db)