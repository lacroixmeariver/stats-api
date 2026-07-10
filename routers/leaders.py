from fastapi import APIRouter
from services import balldontlie as api_service
router = APIRouter()

@router.get("/{stat_type}/{season}")
async def get_stat_leader(stat_type: str, season: int):
    return api_service.get_stat_leaders(stat_type, season)