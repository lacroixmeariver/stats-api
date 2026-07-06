from fastapi import FastAPI
from routers import players, teams, games
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.include_router(players.router, prefix="/players")
app.include_router(teams.router, prefix="/teams")
app.include_router(games.router, prefix="/games")
app.include_router(leaders.router, prefix="/leaders")

