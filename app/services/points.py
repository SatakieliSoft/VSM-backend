from sqlalchemy.orm import Session
from app.models.user import User

def assign_points_to_user(user_id: int, points: int, db: Session) -> User:
    """
    Pridá používateľovi body a vráti aktualizovaný objekt.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("Používateľ neexistuje.")

    user.points += points
    db.commit()
    db.refresh(user)
    return user
