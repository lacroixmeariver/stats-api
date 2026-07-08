from services import api
# just client services and json responses

# ----------------------------------------------------------------
# Player API requests
# ----------------------------------------------------------------

def get_all_players():
    return api.nba.players.list(per_page=25)

def get_player(player_id):
    return api.nba.players.get(player_id)

# ----------------------------------------------------------------
# Team API requests 
# ----------------------------------------------------------------

def get_all_teams():
    return api.nba.teams.list()

def get_team(team_id):
    return api.nba.teams.get(team_id)

# ----------------------------------------------------------------
# Games API requests
# ----------------------------------------------------------------

def get_all_games():
    return api.nba.games.list()

def get_game(game_id):
    return api.nba.teams.get(game_id)


# ----------------------------------------------------------------
# Stat leaders API requests
# ----------------------------------------------------------------

def get_stat_leaders(stat_type, season):
    return api.nba.leaders.get(stat_type=stat_type, season=season)