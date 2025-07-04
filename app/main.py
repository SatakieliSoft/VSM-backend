# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import users, landmarks, routes, auth, visited
from app.db.database import init_db
from app.db.seed_data import seed_demo_data

app = FastAPI(title="Via Sancti Backend Demo")

# ✅ CORS pre frontend na GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://satakielisoft.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔄 Inicializácia databázy a (voliteľné) naplnenie dátami
@app.on_event("startup")
def startup_event():
    init_db()
    # seed_demo_data()  # 👉 odkomentuj len ak potrebuješ demo dáta vložiť pri štarte

# 📦 Registrácia routerov
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(landmarks.router, prefix="/landmarks", tags=["Landmarks"])
app.include_router(routes.router, prefix="/routes", tags=["Routes"])
app.include_router(visited.router, prefix="/visited", tags=["Visited"])

# 🏠 Koreňová cesta
@app.get("/")
def read_root():
    return {"message": "Via Sancti Backend API is running."}
