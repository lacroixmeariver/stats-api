from fastapi import APIRouter
from services import balldontlie

router = APIRouter()

@router.get("/")
async def get_players():
    return {"message" : "get all players"}

@router.get("/{player_id}")
async def get_player(player_id: int):
    return balldontlie.get_player(player_id)

