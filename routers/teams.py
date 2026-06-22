from fastapi import APIRouter
from services import balldontlie as api_service
router = APIRouter()

@router.get("/")
async def get_teams():
    return api_service.get_all_teams()