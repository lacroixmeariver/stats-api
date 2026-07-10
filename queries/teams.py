from database import pool
from psycopg2.extras import RealDictCursor

def upsert_all_teams(all_teams_data):
    conn = pool.getconn()
    cur = conn.cursor()
    for team in all_teams_data:
        cur.execute(
        """ INSERT INTO teams (id, conference, division, city, name, full_name, abbreviation) VALUES
        (%(id)s, %(conference)s, %(division)s, %(city)s, %(name)s, %(full_name)s, %(abbreviation)s) 
        ON CONFLICT (id) DO UPDATE SET
            conference = EXCLUDED.conference,
            division = EXCLUDED.division,
            city = EXCLUDED.city,
            name = EXCLUDED.name,
            full_name = EXCLUDED.full_name,
            abbreviation = EXCLUDED.abbreviation
        """, team)
    conn.commit()
    cur.close()
    pool.putconn(conn)
    
    
def upsert_team(team):
    conn = pool.getconn()
    cur = conn.cursor()
    cur.execute(
        """ INSERT INTO teams (id, conference, division, city, name, full_name, abbreviation) VALUES
        (%(id)s, %(conference)s, %(division)s, %(city)s, %(name)s, %(full_name)s, %(abbreviation)s) 
        ON CONFLICT (id) DO UPDATE SET
            conference = EXCLUDED.conference,
            division = EXCLUDED.division,
            city = EXCLUDED.city,
            name = EXCLUDED.name,
            full_name = EXCLUDED.full_name,
            abbreviation = EXCLUDED.abbreviation
        """, team)
    conn.commit()
    cur.close()
    pool.putconn(conn)

def get_all_teams():
    conn = pool.getconn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    # RealDictCursor allows for the data returned from db to be accessed according to attributes
    cur.execute(
        """ SELECT id, conference, division, city, name, full_name, abbreviation FROM teams; """    
    )
    result = cur.fetchall()
    cur.close()
    pool.putconn(conn)
    return result
    