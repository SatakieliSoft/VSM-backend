from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserRead
from app.services.points import assign_points_to_user

router = APIRouter()

# Získanie databázovej session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Zoznam všetkých používateľov
@router.get("/", response_model=List[UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

# Získanie používateľa podľa ID
@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Vytvorenie nového používateľa
@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Pridanie bodov používateľovi
@router.post("/add-points/{user_id}")
def add_points(user_id: int, points: int, db: Session = Depends(get_db)):
    try:
        user = assign_points_to_user(user_id, points, db)
        return {"message": f"{points} bodov pridaných.", "total": user.points}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
