# app/config.py

import os

SECRET_KEY = os.getenv("SECRET_KEY", "supertajnykluc")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # napr. 60 minút
