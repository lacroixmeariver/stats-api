from fastapi import APIRouter
from services import balldontlie as api_service
router = APIRouter()

@router.get("/")
async def get_games():
    return api_service.get_all_games()

@router.get("/{game_id}")
async def get_game(game_id: int):
    return api_service.get_game(game_id)
