# app/config.py

import os
from pathlib import Path
from dotenv import load_dotenv
from app.logging_config import setup_logging


# Définir le chemin vers le fichier .env (niveau racine)
env_path = Path(__file__).resolve().parent.parent / '.env'

load_dotenv(dotenv_path=env_path)


class Settings:
    GRAPHDB_URL_SELECT: str = os.getenv("GRAPHDB_URL_SELECT", "")
    GRAPHDB_URL_UPDATE: str = os.getenv("GRAPHDB_URL_UPDATE", "")
    GRAPHDB_URL: str = os.getenv("GRAPHDB_URL", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")


settings = Settings()


logger = setup_logging()
logger.info("Configuration chargée.")
