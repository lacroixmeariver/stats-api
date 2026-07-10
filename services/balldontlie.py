import os
from dotenv import load_dotenv
load_dotenv()
from balldontlie import BalldontlieAPI
api = BalldontlieAPI(api_key=os.getenv("BALLDONTLIE_API_KEY"))
