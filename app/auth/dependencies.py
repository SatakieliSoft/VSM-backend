# app/auth/dependencies.py

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.user import User
from app.auth.auth_utils import verify_token  # predpokladaná utilita

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(verify_token), db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.id == token["sub"]).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user
