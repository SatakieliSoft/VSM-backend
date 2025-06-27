import json
from app.db.database import SessionLocal
from app.models.user import User
from app.models.landmark import Landmark
from app.models.route import Route

def seed_demo_data():
    db = SessionLocal()

    # Kontrola, či už dáta existujú
    if db.query(User).first():
        print("Demo data already seeded.")
        db.close()
        return

    # ➕ Načítanie používateľov z JSON súboru
    try:
        with open("data/demo-users.json", encoding="utf-8") as f:
            users = json.load(f)
            for u in users:
                # Odstráň neznáme polia pre SQLAlchemy model, ak existujú
                allowed_fields = {key: u[key] for key in ["id", "username", "full_name", "points"] if key in u}
                user = User(**allowed_fields)
                db.add(user)
    except Exception as e:
        print("Nepodarilo sa načítať používateľov zo súboru:", e)

    # ➕ Pridanie ukážkovej pamiatky
    landmark = Landmark(
        name="Kostol sv. Martina v Tepličke",
        description="Historický kostol zasvätený sv. Martinovi.",
        latitude=49.1510,
        longitude=18.7650
    )
    db.add(landmark)

    # ➕ Pridanie ukážkovej trasy
    route = Route(
        name="Úsek Teplička - Martin",
        description="Krátka pútnická trasa medzi Tepličkou a Martinom.",
        gpx_file="example.gpx"
    )
    db.add(route)

    db.commit()
    db.close()
    print("Demo data seeded.")
