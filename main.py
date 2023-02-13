from fastapi import FastAPI, status, APIRouter
from fastapi.encoders import jsonable_encoder
from database.database import Base, engine
from pydantic import BaseModel
from sqlalchemy.orm import Session
from business_objects.player import Player
from business_objects.league import LeagueModel
from business_objects.team import Team, TeamModel
from business_objects.contract import ContractModel

from service.playerService import PlayerService
from service.teamService import TeamService
from service.leagueService import LeagueService
from service.contractService import ContractService
#from service.leagueService import LeagueService


router = APIRouter()

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()
# <irrelevant code here..>
@app.get("/")
async def root():
    return {"message": "Hello World"}

############################### PLAYER ########################################
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

@app.delete("/player/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["player"])
def delete_player_by_id(id: int):
    playerService = PlayerService()
    player = playerService.get_player_by_id(id)
    if "message" in player:
        return player
    else:
        playerService.delete_player_by_id(id)
        return {"message": f"The player with id {id} has been deleted"}


@app.put("/player/{id}", status_code=status.HTTP_200_OK, tags=["player"])
def put_player_by_id(id: int, player: Player):
    playerService = PlayerService()
    res = playerService.put_player_by_id(id, player)
    return res


############################### TEAM ########################################

@app.post("/team", status_code=status.HTTP_201_CREATED,tags=['team'])
def add_team(team: TeamModel):
    teamService = TeamService()
    res = teamService.add_team(team)
    return res


@app.get("/team/", status_code=status.HTTP_201_CREATED,tags=['team'])
def get_all_teams():
    teamService = TeamService()
    res = teamService.get_all_teams()
    return res

@app.get("/team/{id}", status_code=status.HTTP_201_CREATED,tags=['team'])
def get_team_by_id(id:int):
    teamService = TeamService()
    res = teamService.get_team_by_id(id)
    return res


@app.get("/team/{id}/contracts",status_code=status.HTTP_201_CREATED,tags=['team'])
def get_all_contacts_by_id_team(id : int):
    
    contactService = ContractService()
    res = contactService.get_all_contracts_by_id_team(id)
    return res



@app.delete("/team/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["team"])
def delete_team_by_id(id: int):
    teamService = TeamService()
    team = teamService.get_team_by_id(id)
    if "message" in team:
        return team
    else:
        teamService.delete_team_by_id(id)
        return {"message": f"The team with id {id} has been deleted"}


@app.put("/team/{id}", status_code=status.HTTP_200_OK, tags=["team"])
def put_team_by_id(id: int, team: TeamModel):
    teamService = TeamService()
    res = teamService.put_team_by_id(id, team)
    return res

@app.put("/team/{id}/promotion", status_code=status.HTTP_200_OK, tags=["team"])
def update_team_league_after_promotion(id : int) :
    teamService = TeamService()
    res = teamService.update_team_league_after_promotion(id)
    return res

@app.put("/team/{id}/relegation", status_code=status.HTTP_200_OK, tags=["team"])
def update_team_league_after_relegation(id : int) :
    teamService = TeamService()
    res = teamService.update_team_league_after_relegation(id)
    return res




############################### LEAGUE ########################################


@app.post("/league", status_code=status.HTTP_201_CREATED,tags=['league'])
def add_league(league: LeagueModel):
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

@app.get("/league/{id_league}/teams",status_code=status.HTTP_201_CREATED,tags=['league'])
def get_all_teams_by_id_league(id_league : int) :
    teamService = TeamService()
    res = teamService.get_all_teams_by_id_league(id_league)
    return res

@app.get("/league/{id_league}/contracts",status_code=status.HTTP_201_CREATED,tags=['league'])
def get_all_contract_by_id_league(id_league : int) :
    contractService = ContractService()
    res = contractService.get_all_contracts_by_id_league(id_league)
    return res


@app.put("/league/{id}", status_code=status.HTTP_200_OK, tags=["league"])
def put_league_by_id(id: int, league: LeagueModel):
    leagueService = LeagueService()
    res = leagueService.put_league_by_id(id, league)
    return res


############################### CONTRACT ########################################

@app.post("/contract", status_code=status.HTTP_201_CREATED,tags=['contract'])
def add_cotract(contract: ContractModel):
    contractService = ContractService()
    res = contractService.add_contract(contract)
    return res