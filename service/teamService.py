from dao.teamDAO import TeamDAO
from business_objects.team import Team, TeamModel
from database.database import TeamDB
from datetime import date
from typing import List, Dict
from service.leagueService import LeagueService

class TeamService():
    def __init__(self):
        pass

    def is_valid_id_league(self,id_league):
        try:

            # Compare salary
            if len(LeagueService().get_league_by_id(id_league))>0 :
                return True
            else:
                return False
        except ValueError:
            # Return False if internSalaryGrid is not in the correct format
            return False


    def add_team(self,team:TeamModel) -> str : 
        if not self.is_valid_id_league(team.id_league):
            return f"{team.id_league} is not a valid id league"

        teamDB = TeamDB(name = team.name,id_league = team.id_league)
        dao = TeamDAO()
        id = dao.add_team(teamDB)
        return f"created todo item with id {id}"


    def get_all_teams(self)-> List[Dict]:
        dao = TeamDAO()
        all_teams = dao.get_all_teams()
        res = {"teams": [team.as_dict() for team in all_teams]}
        return res

    def get_team_by_id(self,id:int) -> Dict:
        dao = TeamDAO()
        teamDB = dao.get_team_by_id(id)
        if teamDB:
            return teamDB.as_dict()
        else :
            return {"message":f'The team with id {id} does not exist'}


    def get_all_teams_by_id_league(self,id_league)-> List[Dict]:
        dao = TeamDAO()
        all_teams = dao.get_all_teams_by_id_league(id_league)
        res = {"teams": [team.as_dict() for team in all_teams]}
        return res