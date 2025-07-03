from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.database import Base

class Landmark(Base):
    __tablename__ = "landmarks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    typ = Column(String, nullable=True)
    poloha = Column(String, nullable=True)  # 🆕 napr. mesto
    description = Column(String, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # 🆕 spätný vzťah na navštívenia
    visits = relationship(
        "VisitedLandmark",
        back_populates="landmark",
        cascade="all, delete-orphan"
    )
