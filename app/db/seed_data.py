import json
from app.db.database import SessionLocal
from app.models.user import User
from app.models.landmark import Landmark
from app.models.route import Route
from app.auth.auth_utils import get_password_hash

def seed_demo_data():
    db = SessionLocal()

    # 👉 Kontrola, či už niekto existuje
    if db.query(User).first():
        print("Demo data already seeded.")
        db.close()
        return

    # ➕ Používatelia z JSON
    try:
        with open("data/demo-users.json", encoding="utf-8") as f:
            users = json.load(f)
            for u in users:
                allowed_fields = {key: u[key] for key in ["id", "email", "full_name", "points"] if key in u}
                allowed_fields["hashed_password"] = get_password_hash(u["password"])
                user = User(**allowed_fields)
                db.add(user)
    except Exception as e:
        print("❌ Nepodarilo sa načítať používateľov:", e)

    # ➕ Pamiatky z JSON (nepovinné – ak máš súbor landmarks.json)
    try:
        with open("data/landmarks.json", encoding="utf-8") as f:
            landmarks = json.load(f)
            for l in landmarks:
                allowed_fields = {key: l[key] for key in ["name", "description", "latitude", "longitude"]}
                landmark = Landmark(**allowed_fields)
                db.add(landmark)
    except Exception as e:
        print("⚠️ Nepodarilo sa načítať pamiatky:", e)

    # ➕ Trasy z JSON
    try:
        with open("data/routes.json", encoding="utf-8") as f:
            routes = json.load(f)
            for r in routes:
                allowed_fields = {key: r[key] for key in ["name", "description", "gpx_file"]}
                route = Route(**allowed_fields)
                db.add(route)
    except Exception as e:
        print("⚠️ Nepodarilo sa načítať trasy:", e)

    # 💾 Uloženie
    db.commit()
    db.close()
    print("✅ Demo data seeded.")
