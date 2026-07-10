from balldontlie.nba.models import NBAPlayer, NBATeam
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
