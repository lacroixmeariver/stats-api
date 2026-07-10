from dotenv import load_dotenv
load_dotenv()
import os
from psycopg2.pool import SimpleConnectionPool

# switched to pool from a shared connection to reduce overhead
pool = SimpleConnectionPool(
    2, 10,
    host="localhost",
    dbname="stats_db",
    user="ingrid",
    password=os.getenv('DB_PASS')
)
