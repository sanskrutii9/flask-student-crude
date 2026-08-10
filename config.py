import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "fallback-secret-key"

    # Set up absolute path within the project root
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    if os.environ.get("RAILWAY_ENVIRONMENT"):
        # Store in /tmp or create an absolute path in current app directory
        db_path = os.path.join(BASE_DIR, "students.db")
    else:
        db_path = os.path.join(BASE_DIR, "students.db")

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False