import os
from balldontlie import BalldontlieAPI
api = BalldontlieAPI(api_key=os.getenv("BALLDONTLIE_API_KEY"))
base_url = os.getenv("BASE_URL")

def get_player(player_id):
    return api.nba.players.get(player_id)

