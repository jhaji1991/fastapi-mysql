from fastapi import FastAPI
from app.api import user
from app.core.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(user.router)