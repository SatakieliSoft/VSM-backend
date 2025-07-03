from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import users, landmarks, routes, auth, visited
from app.db.database import init_db
from app.db.seed_data import seed_demo_data

app = FastAPI(title="Via Sancti Backend Demo")

# ✅ CORS pre GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://satakielisoft.github.io"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

# 🔄 Inicializácia databázy a naplnenie dátami
init_db()
seed_demo_data()

# 📦 Registrácia routerov
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(landmarks.router, prefix="/landmarks", tags=["Landmarks"])
app.include_router(routes.router, prefix="/routes", tags=["Routes"])
app.include_router(visited.router, prefix="/visited", tags=["Visited"])  # 🆕 pridanie

# 🏠 Koreňová cesta
@app.get("/")
def read_root():
    return {"message": "Via Sancti Backend API is running."}
