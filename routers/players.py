from fastapi import APIRouter
#from ingestion import client as api_service
from queries.players import get_all_players as db_get_players
router = APIRouter()

@router.get("/")
async def get_players():
    return db_get_players()

@router.get("/{player_id}")
async def get_player(player_id: int):
    # return api_service.get_player(player_id)
    return
    # TODO Add specific player db query

