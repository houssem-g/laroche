# app/config.py

import os
from pathlib import Path
from dotenv import load_dotenv

# Définir le chemin vers le fichier .env (niveau racine)
env_path = Path(__file__).resolve().parent.parent / '.env'

load_dotenv(dotenv_path=env_path)


class Settings:
    GRAPHDB_URL_SELECT: str = os.getenv("GRAPHDB_URL_SELECT", "")
    GRAPHDB_URL_UPDATE: str = os.getenv("GRAPHDB_URL_UPDATE", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")


settings = Settings()
