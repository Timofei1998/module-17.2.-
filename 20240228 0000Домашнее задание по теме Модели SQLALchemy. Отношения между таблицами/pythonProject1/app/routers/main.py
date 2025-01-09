from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.backend.db import SessionLocal, engine, Base
from app.models import User, Task

router = APIRouter()

# Инициализация базы данных
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_root():
    return {"message": "Welcome to Task Manager!"}
