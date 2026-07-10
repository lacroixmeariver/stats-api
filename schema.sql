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
    home_team_score INTEGER,
    visitor_team_score INTEGER,
    home_team_id INTEGER,
    visitor_team_id INTEGER,
    FOREIGN KEY (home_team_id) REFERENCES teams(id),
    FOREIGN KEY (visitor_team_id) REFERENCES teams(id)
);