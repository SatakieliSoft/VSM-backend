import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Načítaj PostgreSQL URL z prostredia (Render → Environment → DATABASE_URL)
DATABASE_URL2 = os.getenv("DATABASE_URL2", "postgresql://vsm_issn_user:KWbToV8dhEclg6t4GERDPSE3OUDDzqJO@dpg-d1jqali4d50c738coe6g-a/vsm_issn")

# Inicializácia engine
engine = create_engine(DATABASE_URL)

# Session pre použitie v route-funkciách
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Základná trieda pre modely
Base = declarative_base()

# Import modelov + vytvorenie tabuliek
def init_db():
    from app.models import user, landmark, route
    Base.metadata.create_all(bind=engine)

# Dependency pre získanie DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
