from pathlib import Path
from database import pool

schema_path = Path(__file__).parent/"schema.sql"
with open(schema_path, "r") as file:
    conn = pool.getconn()
    cur = conn.cursor()
    cur.execute(file.read())
    conn.commit()
    pool.putconn(conn)
