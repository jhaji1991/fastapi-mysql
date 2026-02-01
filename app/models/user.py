from sqlalchemy import Column, Integer, String
from app.core.database import Base

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True, index=True)
    phone = Column(String(20))
    city = Column(String(50))
    country = Column(String(50))