from pathlib import Path
from database import cur, conn

schema_path = Path(__file__).parent/"schema.sql"
with open(schema_path, "r") as file:
    cur.execute(file.read())

conn.commit()
