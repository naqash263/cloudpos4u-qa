import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL")
    API_BASE_URL = os.getenv("API_BASE_URL")

    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_SCHEMA = os.getenv("DB_SCHEMA")

    RUN_DB_TESTS = os.getenv("RUN_DB_TESTS", "false").lower() == "true"

    AI_TEST_PROVIDER = os.getenv("AI_TEST_PROVIDER", "")
    AI_TEST_MODEL = os.getenv("AI_TEST_MODEL", "")
    AI_TEST_API_KEY = os.getenv("AI_TEST_API_KEY", "")

    AI_EMBEDDING_API_KEY = os.getenv("AI_EMBEDDING_API_KEY", "")
    AI_EMBEDDING_MODEL = os.getenv(
        "AI_EMBEDDING_MODEL",
        "text-embedding-3-small"
    )