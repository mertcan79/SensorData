import os
from pathlib import Path
from pydantic import BaseSettings
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    PROJECT_NAME: str = "Sensors"
    PROJECT_VERSION: str = "1.0.0"

    USE_SQLITE_DB: str = False
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD = '123'
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_PORT: str = '5432'
    POSTGRES_DB: str = 'db'
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = '123'
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 240

    TEST_USER_EMAIL = "test@example.com"
