from fastapi import APIRouter
#from services import balldontlie as api_service
from queries.teams import get_all_teams as db_all_teams
router = APIRouter()

@router.get("/")
async def get_all_teams():
    #return api_service.get_all_teams()
    return db_all_teams()