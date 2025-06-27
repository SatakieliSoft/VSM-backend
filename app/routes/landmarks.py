from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import SessionLocal
from app.models.landmark import Landmark
from app.schemas.landmark import LandmarkCreate, LandmarkRead

router = APIRouter()

# Dependency na získanie databázovej session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Získanie všetkých pamiatok
@router.get("/", response_model=List[LandmarkRead])
def read_landmarks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Landmark).offset(skip).limit(limit).all()

# Získanie konkrétnej pamiatky podľa ID
@router.get("/{landmark_id}", response_model=LandmarkRead)
def read_landmark(landmark_id: int, db: Session = Depends(get_db)):
    landmark = db.query(Landmark).filter(Landmark.id == landmark_id).first()
    if not landmark:
        raise HTTPException(status_code=404, detail="Landmark not found")
    return landmark

# Pridanie novej pamiatky (napr. cez admin rozhranie)
@router.post("/", response_model=LandmarkRead)
def create_landmark(landmark: LandmarkCreate, db: Session = Depends(get_db)):
    db_landmark = Landmark(**landmark.dict())
    db.add(db_landmark)
    db.commit()
    db.refresh(db_landmark)
    return db_landmark
