from pydantic import BaseModel
from datetime import datetime

# Vstupná schéma pre označenie pamiatky ako navštívenej
class VisitedLandmarkCreate(BaseModel):
    landmark_id: int

# Výstupná schéma pre zobrazenie jednej navštívenej pamiatky
class VisitedLandmarkRead(BaseModel):
    id: int
    landmark_id: int
    user_id: int
    timestamp: datetime

    class Config:
        orm_mode = True
