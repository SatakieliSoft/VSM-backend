from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, landmarks, routes, auth
from app.db.database import init_db

app = FastAPI(title="Via Sancti Backend Demo")

# ✅ Povolenie CORS pre GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://satakielisoft.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializácia databázy
init_db()

# Registrácia routerov
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(landmarks.router, prefix="/landmarks", tags=["Landmarks"])
app.include_router(routes.router, prefix="/routes", tags=["Routes"])

@app.get("/")
def read_root():
    return {"message": "Via Sancti Backend API is running."}
