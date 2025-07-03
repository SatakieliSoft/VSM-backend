from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.models.landmark import Landmark
from app.models.visited import VisitedLandmark
from app.schemas.visited import VisitedLandmarkCreate, VisitedLandmarkRead
from app.auth.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=VisitedLandmarkRead)
def mark_landmark_as_visited(
    data: VisitedLandmarkCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Overenie, či pamiatka existuje
    landmark = db.query(Landmark).filter(Landmark.id == data.landmark_id).first()
    if not landmark:
        raise HTTPException(status_code=404, detail="Pamiatka neexistuje.")

    # Overenie, či už bola navštívená
    existing = db.query(VisitedLandmark).filter_by(
        user_id=current_user.id,
        landmark_id=data.landmark_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Pamiatka už bola označená ako navštívená.")

    # Vytvorenie záznamu
    visit = VisitedLandmark(user_id=current_user.id, landmark_id=data.landmark_id)
    db.add(visit)

    # Pripočítanie bodu
    current_user.points += 1

    db.commit()
    db.refresh(visit)
    return visit


@router.get("/", response_model=list[VisitedLandmarkRead])
def get_visited_landmarks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    visits = db.query(VisitedLandmark).filter_by(user_id=current_user.id).all()
    return visits
