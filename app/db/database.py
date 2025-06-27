from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cesta k SQLite databáze
DATABASE_URL = "sqlite:///./via_sancti.db"

# Vytvorenie engine s podporou SQLite (nutné pridať connect_args)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Konfigurácia session (pripojenie k DB pre každú operáciu)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Základná trieda pre modely
Base = declarative_base()

# Funkcia na inicializáciu (vytvorenie tabuliek)
def init_db():
    from app.models import user, landmark, route  # import modelov, aby SQLAlchemy vedel o tabuľkách
    Base.metadata.create_all(bind=engine)
