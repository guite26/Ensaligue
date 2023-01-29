from dao.leagueDAO import LeagueDAO
from business_objects.league import League
from database.database import LeagueDB
from datetime import date
from typing import List, Dict

class LeagueService():
    def __init__(self):
        pass

    def is_valid_intern_salary_grid(self,internSalaryGrid):
        try:
            # Compare salary
            if (internSalaryGrid[0]<internSalaryGrid[1]) & (internSalaryGrid[1]<internSalaryGrid[2]) :
                return True
            else:
                return False
        except ValueError:
            # Return False if internSalaryGrid is not in the correct format
            return False




    def add_league(self,league:League) -> str : 
        if not self.is_valid_intern_salary_grid(league.internSalaryGrid):
            return f"{league.internSalaryGrid} is not a valid internSalaryGrid"

        leagueDB = LeagueDB(name = league.name,country = league.country,level=league.level,professional_minimum_wage=league.professional_minimum_wage,daily_salary_first_year = league.internSalaryGrid[0],daily_salary_second_year=league.internSalaryGrid[1],daily_salary_third_year=league.internSalaryGrid[2])
        dao = LeagueDAO()
        id = dao.add_league(leagueDB)
        return f"created todo item with id {id}"



    def get_all_leagues(self)-> List[Dict]:
        dao = LeagueDAO()
        all_leagues = dao.get_all_leagues()
        res = {"leagues": [league.as_dict() for league in all_leagues]}
        return res

    def get_league_by_id(self,id:int) -> LeagueDB:
        dao = LeagueDAO()
        leagueDB = dao.get_league_by_id(id)
        if leagueDB:
            return leagueDB.as_dict()
        else :
            return {"message":f'The league with id {id} does not exist'}


    
            



    