from pydantic import BaseModel

class LandmarkBase(BaseModel):
    name: str
    description: str | None = None
    latitude: float
    longitude: float

class LandmarkCreate(LandmarkBase):
    pass

class LandmarkRead(LandmarkBase):
    id: int

    class Config:
        orm_mode = True
