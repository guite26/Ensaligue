from fastapi import FastAPI, status, APIRouter
from fastapi.encoders import jsonable_encoder
from database.database import Base, engine, PlayerDB
from pydantic import BaseModel
from sqlalchemy.orm import Session
from business_objects.player import Player
from service.playerService import PlayerService

router = APIRouter()

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()
# <irrelevant code here..>
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/player", status_code=status.HTTP_201_CREATED,tags=['player'])
def add_player(player: Player):
    playerService = PlayerService()
    res = playerService.add_player(player)
    return res

@app.get("/player/{id}", status_code=status.HTTP_201_CREATED,tags=['player'])
def get_player_by_id(id:int):
    playerService = PlayerService()
    res = playerService.get_player_by_id(id)
    return res

@app.get("/player/", status_code=status.HTTP_201_CREATED,tags=['player'])
def get_all_players():
    playerService = PlayerService()
    res = playerService.get_all_players()
    return res
    