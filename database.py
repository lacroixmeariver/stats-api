import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os
from pathlib import Path

conn = psycopg2.connect(host="localhost", dbname="stats_db", user="ingrid", password=os.getenv("DB_PASS"))
cur = conn.cursor()
