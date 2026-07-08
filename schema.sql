CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL, 
    position VARCHAR(10) NOT NULL,
    height VARCHAR(10) NOT NULL,
    weight VARCHAR(10) NOT NULL,
    jersey_number VARCHAR(10) NOT NULL,
    college VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    draft_year INTEGER,
    draft_round INTEGER,
    draft_number INTEGER
);

CREATE TABLE IF NOT EXISTS (
    id INTEGER PRIMARY KEY,
    conference VARCHAR(15),
    division VARCHAR(15),
    city VARCHAR(15),
    name VARCHAR(50),
    full_name VARCHAR(50),
    abbreviation VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS (
    id INTEGER PRIMARY KEY,
    date VARCHAR(20),
    season INTEGER,
    status VARCHAR(50),
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
);