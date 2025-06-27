# ViaSanctiMartini – Backend

Produkčný backend pre aplikáciu **ViaSanctiMartini.apk** (Android 8+, Kotlin) postavený na FastAPI.  
Obsahuje podporu pre:

- ✅ Registráciu a prihlásenie používateľov (e-mail + heslo)
- ✅ Bezpečné hashovanie hesla pomocou bcrypt
- ✅ JWT token autentifikáciu
- ✅ Správu používateľských bodov
- ✅ Informácie o pamiatkach (landmarks)
- ✅ Správu pútnických trás (routes)
- ✅ Seedovanie ukážkových dát (users, routes, landmarks)
- ✅ Pripravené pre nasadenie na Railway

---

## 🚀 Inštalácia lokálne

```bash
git clone https://github.com/tvoje-meno/viasancti-backend.git
cd viasancti-backend
pip install -r requirements.txt
uvicorn app.main:app --reload
