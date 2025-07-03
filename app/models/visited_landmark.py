from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class VisitedLandmark(Base):
    __tablename__ = "visited_landmarks"
    __table_args__ = (UniqueConstraint("user_id", "landmark_id", name="unique_user_landmark"),)

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    landmark_id = Column(Integer, ForeignKey("landmarks.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="visited_landmarks")
    landmark = relationship("Landmark", back_populates="visits")
