from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    gpx_file = Column(String, nullable=True)  # názov alebo cesta k GPX súboru
