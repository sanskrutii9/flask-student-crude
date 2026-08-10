import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "fallback-secret-key"

    if os.environ.get("RAILWAY_ENVIRONMENT"):
        SQLALCHEMY_DATABASE_URI = "sqlite:////data/students.db"
    else:
        SQLALCHEMY_DATABASE_URI = "sqlite:///students.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False