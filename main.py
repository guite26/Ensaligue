from fastapi import FastAPI, status, APIRouter
from fastapi.encoders import jsonable_encoder
from database.database import Base, engine, PlayerDB , InternSalaryGridDB, LeagueDB
from pydantic import BaseModel
from sqlalchemy.orm import Session
from business_objects.player import Player
from business_objects.internSalaryGrid import InternSalaryGrid
from business_objects.league import League
from service.playerService import PlayerService
from service.internSalaryGridService import InternSalaryGridService
from service.leagueService import LeagueService


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


@app.post("/internSalaryGrid", status_code=status.HTTP_201_CREATED,tags=['internSalaryGrid'])
def add_internSalaryGrid(internSalaryGrid: InternSalaryGrid):
    internSalaryGridService = InternSalaryGridService()
    res = internSalaryGridService.add_internSalaryGrid(internSalaryGrid)
    return res

@app.get("/internSalaryGrid/{id}", status_code=status.HTTP_201_CREATED,tags=['internSalaryGrid'])
def get_internSalaryGrid_by_id(id:int):
    internSalaryGridService = InternSalaryGridService()
    res = internSalaryGridService.get_internSalaryGrid_by_id(id)
    return res

@app.get("/internSalaryGrid/", status_code=status.HTTP_201_CREATED,tags=['internSalaryGrid'])
def get_all_internSalaryGrid():
    internSalaryGridService = InternSalaryGridService()
    res = internSalaryGridService.get_all_internSalaryGrid()
    return res


@app.post("/league", status_code=status.HTTP_201_CREATED,tags=['league'])
def add_team(league: League):
    LeagueService = LeagueService()
    res = LeagueService.add_league(league)
    return res