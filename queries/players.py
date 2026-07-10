from database import pool

def upsert_single_player(player):
    conn = pool.getconn()
    cur = conn.cursor()
    cur.execute(
        """ INSERT INTO players (id, first_name, last_name, position, height,
        weight, jersey_number, college, country, draft_year, draft_round, draft_number, team_id) VALUES
        (%(id)s, %(first_name)s, %(last_name)s, %(position)s, %(height)s, %(weight)s, %(jersey_number)s, 
        %(college)s, %(country)s, %(draft_year)s, %(draft_round)s, %(draft_number)s, %(team_id)s) 
        ON CONFLICT (id) DO UPDATE SET
            first_name = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name,
            position = EXCLUDED.position,
            height = EXCLUDED.height,
            weight = EXCLUDED.weight,
            jersey_number = EXCLUDED.jersey_number,
            college = EXCLUDED.college,
            country = EXCLUDED.country,
            draft_year = EXCLUDED.draft_year,
            draft_round = EXCLUDED.draft_round,
            draft_number = EXCLUDED.draft_number,
            team_id = EXCLUDED.team_id 
        """, player)
    conn.commit()
    cur.close()
    pool.putconn(conn)


def upsert_all_players(all_players_data):
    conn = pool.getconn()
    cur = conn.cursor()
    for player in all_players_data:
        cur.execute(
        """ INSERT INTO players (id, first_name, last_name, position, height,
        weight, jersey_number, college, country, draft_year, draft_round, draft_number, team_id) VALUES
        (%(id)s, %(first_name)s, %(last_name)s, %(position)s, %(height)s, %(weight)s, %(jersey_number)s, 
        %(college)s, %(country)s, %(draft_year)s, %(draft_round)s, %(draft_number)s, %(team_id)s) 
        ON CONFLICT (id) DO UPDATE SET
            first_name = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name,
            position = EXCLUDED.position,
            height = EXCLUDED.height,
            weight = EXCLUDED.weight,
            jersey_number = EXCLUDED.jersey_number,
            college = EXCLUDED.college,
            country = EXCLUDED.country,
            draft_year = EXCLUDED.draft_year,
            draft_round = EXCLUDED.draft_round,
            draft_number = EXCLUDED.draft_number,
            team_id = EXCLUDED.team_id 
        """, player)
    conn.commit()
    cur.close()
    pool.putconn(conn)
    
