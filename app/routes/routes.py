from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import SessionLocal
from app.models.route import Route
from app.schemas.route import RouteCreate, RouteRead

router = APIRouter()

# 🔄 Získanie databázovej session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📋 Zoznam všetkých trás
@router.get("/", response_model=List[RouteRead])
def read_routes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Route).offset(skip).limit(limit).all()

# 🔍 Získanie trasy podľa ID
@router.get("/{route_id}", response_model=RouteRead)
def read_route(route_id: int, db: Session = Depends(get_db)):
    route = db.query(Route).filter(Route.id == route_id).first()
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    return route

# ➕ Vytvorenie novej trasy
@router.post("/", response_model=RouteRead)
def create_route(route: RouteCreate, db: Session = Depends(get_db)):
    db_route = Route(**route.dict())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route
