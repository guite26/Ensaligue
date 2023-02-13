from database.database import TeamDB, engine, session, LeagueDB
from sqlalchemy.orm import Query
from typing import List
from business_objects.team import TeamModel
from dao.leagueDAO import LeagueDAO

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
    
    def get_all_teams_by_id_league(self, id_league: int) -> List[TeamDB]:
        teamdb = session.query(TeamDB).filter_by(TeamDB.id_league == id_league).all()
        return teamdb


    def delete_team_by_id(self, id: int) -> None:
        team = session.query(TeamDB).filter_by(id_team=id).first()
        if team:
            session.delete(team)
            session.commit()
        else:
            raise Exception("Team with id {} not found.".format(id))


    def put_team_by_id(self, id: int, team: TeamDB) -> TeamDB:
        team_to_update = session.query(TeamDB).get(id)
        if team_to_update:
            team_to_update.update(team.__dict__)
            session.commit()
        return team_to_update

    def put_team_by_id(self, existing_team : TeamDB, new_team : TeamModel) -> TeamDB:
        existing_team.name = new_team.name
        existing_team.id_league = new_team.id_league
        session.commit()
        return existing_team
    

    def update_team_league_after_promotion(self,existing_team : TeamDB,curently_league : LeagueDB) -> TeamDB :
        existing_team.id_league = LeagueDAO().get_new_id_league_after_promotion(curently_league)
        session.commit()
        return existing_team
    
    def update_team_league_after_relegation(self,existing_team : TeamDB,curently_league : LeagueDB) -> TeamDB :
        existing_team.id_league = LeagueDAO().get_new_id_league_after_promotion(curently_league)
        session.commit()
        return existing_team

