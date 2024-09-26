import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

# Postgres credentials
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", 5432)  # Default PostgreSQL port is 5432
DB_NAME = os.getenv("DB_NAME")

BASE_URL = "https://api.themoviedb.org/3"
