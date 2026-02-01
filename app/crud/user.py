from sqlalchemy.orm import Session
from app.models.user import UserDB
from app.schemas.user import User

def get_users(db: Session):
    return db.query(UserDB).all()

def get_user(db: Session, user_id: int):
    return db.query(UserDB).filter(UserDB.id == user_id).first()

def create_user(db: Session, user: User):
    db_user = UserDB(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, updated_user: User):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if user:
        for key, value in updated_user.dict().items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user