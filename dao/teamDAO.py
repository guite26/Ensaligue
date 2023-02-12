from database.database import TeamDB, engine, session
from sqlalchemy.orm import Query
from typing import List

class TeamDAO():
    def __init__(self):
        pass

    def add_team(self,team:TeamDB):
        # add it to the session and commit it
        session.add(team)
        session.commit()
        # grab the id given to the object from the database
        id = team.id_team
        # close the session
        return id

    def get_team_by_id(self,id:int) -> TeamDB:
        # add it to the session and commit it
        teamdb = session.get(entity=TeamDB,ident=id)
        session.commit()
        return teamdb

    def get_all_teams(self) -> List[TeamDB] :
        # add it to the session and commit it
        all_teams = session.query(TeamDB).all()
        return all_teams
    
    def get_all_teams_by_id_league(self,id_league:int) -> List[TeamDB] :
        teamdb = session.get(entity=TeamDB,id_league=id_league)
        session.commit()
        return teamdb

