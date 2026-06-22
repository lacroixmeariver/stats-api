from fastapi import APIRouter
from services import balldontlie as api_service
router = APIRouter()

@router.get("/")
async def get_players():
    return api_service.get_all_players()

@router.get("/{player_id}")
async def get_player(player_id: int):
    return api_service.get_player(player_id)

