from balldontlie.nba.models import NBAPlayer, NBATeam, NBAGame
# purely transformation and handling of raw data -> dictionary following defined data model

# balldontlie sdk returns an object of class NBAPlayer 
def transform_player(raw: NBAPlayer) -> dict:
    return {
        "id": raw.id,
        "first_name": raw.first_name,
        "last_name": raw.last_name,
        "position": raw.position,
        "height": raw.height,
        "weight": raw.weight,
        "jersey_number": raw.jersey_number,
        "college": raw.college,
        "country": raw.country,
        "draft_year": raw.draft_year,
        "draft_round": raw.draft_round,
        "draft_number": raw.draft_number,
        "team_id": raw.team.id if raw.team else None
    }

def transform_team(raw: NBATeam) -> dict:
    return {
        "id": raw.id,
        "conference": raw.conference,
        "division": raw.division,
        "city": raw.city,
        "name": raw.name,
        "full_name": raw.full_name,
        "abbreviation": raw.abbreviation
    }

def transform_all_players(raw_players: list[NBAPlayer]) -> list[dict]:
    players = []
    for player in raw_players:
        players.append(transform_player(player))
    return players

def transform_all_teams(raw_teams: list[NBATeam]) -> list[dict]:
    teams = []
    for team in raw_teams:
        teams.append(transform_team(team))
    return teams


def transform_game(raw: NBAGame) -> dict:
    return {
        "id": raw.id,
        "date": raw.date,
        "season": raw.season,
        "status": raw.status,
        "period": raw.period,
        "time": raw.time,
        "postseason": raw.postseason,
        "home_team_score": raw.home_team_score,
        "visitor_team_score": raw.visitor_team_score,
        "home_team_id": raw.home_team.id,
        "visitor_team_id": raw.visitor_team.id
    }