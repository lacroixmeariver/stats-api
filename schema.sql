CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY,
    conference VARCHAR(15),
    division VARCHAR(15),
    city VARCHAR(15),
    name VARCHAR(50),
    full_name VARCHAR(50),
    abbreviation VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100), 
    position VARCHAR(10),
    height VARCHAR(10),
    weight VARCHAR(10),
    jersey_number VARCHAR(10),
    college VARCHAR(50),
    country VARCHAR(50),
    draft_year FLOAT,
    draft_round FLOAT,
    draft_number FLOAT,
    team_id INTEGER, 
    FOREIGN KEY (team_id) REFERENCES teams(id)
);



CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    date VARCHAR(20),
    season INTEGER,
    status VARCHAR(100),
    period INTEGER,
    time VARCHAR(50),
    postseason BOOLEAN,
    postponed BOOLEAN,
    home_team_score INTEGER,
    visitor_team_score INTEGER,
    datetime VARCHAR(100),
    home_q1 INTEGER DEFAULT 0,
    home_q2 INTEGER DEFAULT 0,
    home_q3 INTEGER DEFAULT 0,
    home_q4 INTEGER DEFAULT 0,
    home_ot1 INTEGER,
    home_ot2 INTEGER,
    home_ot3 INTEGER,
    home_timeouts_remaining INTEGER,
    home_in_bonus BOOLEAN,
    visitor_q1 INTEGER DEFAULT 0,
    visitor_q2 INTEGER DEFAULT 0,
    visitor_q3 INTEGER DEFAULT 0,
    visitor_q4 INTEGER DEFAULT 0,
    visitor_ot1 INTEGER,
    visitor_ot2 INTEGER,
    visitor_ot3 INTEGER,
    visitor_timeouts_remaining INTEGER,
    visitor_in_bonus BOOLEAN,
    ist_stage VARCHAR(50),
    home_team_id INTEGER,
    visitor_team_id INTEGER,
    FOREIGN KEY (home_team_id) REFERENCES teams(id),
    FOREIGN KEY (visitor_team_id) REFERENCES teams(id)
);