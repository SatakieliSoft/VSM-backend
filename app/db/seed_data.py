import json
from app.db.database import SessionLocal
from app.models.user import User
from app.models.landmark import Landmark
from app.models.route import Route
from app.auth.auth_utils import get_password_hash

def seed_demo_data():
    db = SessionLocal()

    # ➕ Používatelia
    if not db.query(User).first():
        try:
            with open("data/demo-users.json", encoding="utf-8") as f:
                users = json.load(f)
                for u in users:
                    allowed_fields = {key: u[key] for key in ["id", "email", "full_name", "points"] if key in u}
                    allowed_fields["hashed_password"] = get_password_hash(u["password"])
                    user = User(**allowed_fields)
                    db.add(user)
            print(f"✅ Používatelia: {len(users)} načítaní")
        except Exception as e:
            print("❌ Chyba pri načítaní používateľov:", e)
    else:
        print("ℹ️ Používatelia už existujú, preskakujem.")

    # ➕ Pamiatky (landmarks)
    if not db.query(Landmark).first():
        try:
            with open("data/landmarks.json", encoding="utf-8") as f:
                landmarks = json.load(f)
                for l in landmarks:
                    allowed_fields = {key: l[key] for key in ["id", "name", "description", "latitude", "longitude"]}
                    landmark = Landmark(**allowed_fields)
                    db.add(landmark)
            print(f"✅ Pamiatky: {len(landmarks)} načítaných")
        except Exception as e:
            print("⚠️ Chyba pri načítaní pamiatok:", e)
    else:
        print("ℹ️ Pamiatky už existujú, preskakujem.")

    # ➕ Trasy (routes)
    if not db.query(Route).first():
        try:
            with open("data/routes.json", encoding="utf-8") as f:
                routes = json.load(f)
                for r in routes:
                    allowed_fields = {key: r[key] for key in ["name", "description", "gpx_file"]}
                    route = Route(**allowed_fields)
                    db.add(route)
            print(f"✅ Trasy: {len(routes)} načítaných")
        except Exception as e:
            print("⚠️ Chyba pri načítaní trás:", e)
    else:
        print("ℹ️ Trasy už existujú, preskakujem.")

    db.commit()
    db.close()
    print("🎉 Seed hotový.")
