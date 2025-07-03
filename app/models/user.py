from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    username = Column(String, unique=True, index=True, nullable=True)
    full_name = Column(String, nullable=True)
    points = Column(Integer, default=0)

    # 🆕 Navštívené pamiatky (1:N)
    visited_landmarks = relationship(
        "VisitedLandmark",
        back_populates="user",
        cascade="all, delete-orphan"
    )
