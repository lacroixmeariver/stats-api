from queries.teams import upsert_team, upsert_all_teams
from queries.players import upsert_single_player, upsert_all_players
from ingestion.client import get_all_teams, get_team, get_player, get_all_players
from ingestion.transform import transform_team, transform_all_teams, transform_player, transform_all_players

# load.py acts as a controller calling the appropriate functions in order to insert/upsert data into the db
# purely for orchestrating the flow of information from the API to the database

def load_in_all_teams():
    all_teams_data = get_all_teams().data
    teams = transform_all_teams(all_teams_data)
    upsert_all_teams(teams)

def load_in_single_team(team_id):
    team_data = get_team(team_id).data
    team = transform_team(team_data)
    upsert_team(team)

def load_in_single_player(player_id):
    player_data = get_player(player_id).data
    player = transform_player(player_data)
    upsert_single_player(player)

# need the paid tier to access 
# def load_in_all_active_players():
#     active_players_data = get_all_active_players().data
#     active_players = transform_all_players(active_players_data)
#     upsert_all_players(active_players)

# includes non active players 
# note: get_all_players() currently set to return 25 entries per page
def load_in_all_players():
    all_players_data = get_all_players().data
    player_data = transform_all_players(all_players_data)
    upsert_all_players(player_data)