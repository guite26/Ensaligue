from database.database import LeagueDB, engine, session
from sqlalchemy.orm import Query
from typing import List
from business_objects.league import LeagueModel

class LeagueDAO():
    def __init__(self):
        pass

    def add_league(self,league:LeagueDB):
        # add it to the session and commit it
        session.add(league)
        session.commit()
        # grab the id given to the object from the database
        id = league.id_league
        # close the session
        return id

    def get_league_by_id(self,id:int) -> LeagueDB:
        # add it to the session and commit it
        leaguedb = session.get(entity=LeagueDB,ident=id)

        return leaguedb

    def get_new_league_after_promotion(self,league_currently : LeagueDB) -> LeagueDB:
        league = session.query(LeagueDB).filter_by(country = league_currently.country, level = league_currently.level -1 ).first()
        return league

    def get_new_league_after_relegation(self,league_currently : LeagueDB) -> LeagueDB:
        league = session.query(LeagueDB).filter_by(country = league_currently.country, level = league_currently.level +1 ).first()
        return league

    def get_all_leagues(self) -> List[LeagueDB] :
        # add it to the session and commit it
        all_leagues = session.query(LeagueDB).all()
        return all_leagues


    def delete_league_by_id(self,id_league:int):
        league = session.query(LeagueDB).filter_by(id_league=id_league).first()
        session.delete(league)
        session.commit()



    def put_league_by_id(self, existing_league : LeagueDB, new_league : LeagueModel) -> LeagueDB:
        existing_league.name = new_league.name
        existing_league.country = new_league.country
        existing_league.level = new_league.level
        existing_league.professional_minimum_wage = new_league.professional_minimum_wage
        existing_league.daily_salary_first_year = new_league.internSalaryGrid[0]
        existing_league.daily_salary_second_year = new_league.internSalaryGrid[1]
        existing_league.daily_salary_third_year = new_league.internSalaryGrid[2]
        session.commit()
        return existing_league
    


