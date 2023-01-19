from fastapi import FastAPI, status, APIRouter
from fastapi.encoders import jsonable_encoder
from database.database import Base, engine, PlayerDB , InternSalaryGridDB, LeagueDB
from pydantic import BaseModel
from sqlalchemy.orm import Session
from business_objects.player import Player
from business_objects.league import League
from business_objects.team import Team
from service.playerService import PlayerService
from service.leagueService import LeagueService
from service.teamService import TeamService

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



@app.post("/league", status_code=status.HTTP_201_CREATED,tags=['league'])
def add_league(league: League):
    leagueService = LeagueService()
    res = leagueService.add_league(league)
    return res




@app.get("/league/{id}", status_code=status.HTTP_201_CREATED,tags=['league'])
def get_league_by_id(id:int):
    leagueService = LeagueService()
    res = leagueService.get_league_by_id(id)
    return res



@app.get("/league/", status_code=status.HTTP_201_CREATED,tags=['league'])
def get_all_leagues():
    leagueService = LeagueService()
    res = leagueService.get_all_leagues()
    return res


@app.post("/team", status_code=status.HTTP_201_CREATED,tags=['team'])
def add_team(team: Team):
    teamService = TeamService()
    res = teamService.add_team(team)
    return res

@app.get("/team/{id}", status_code=status.HTTP_201_CREATED,tags=['team'])
def get_team_by_id(id:int):
    teamService = TeamService()
    res = teamService.get_team_by_id(id)
    return res

@app.get("/team/", status_code=status.HTTP_201_CREATED,tags=['team'])
def get_all_teams():
    teamService = TeamService()
    res = teamService.get_all_teams()
    return res


@app.get("/team/{id_league}", status_code=status.HTTP_201_CREATED,tags=['team'])
def get_all_teams_by_id_league(id_league :int):
    teamService = TeamService()
    res = teamService.get_all_teams_by_id_league()
    return res

