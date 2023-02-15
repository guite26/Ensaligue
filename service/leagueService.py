from dao.leagueDAO import LeagueDAO
from dao.contractDAO import ContractDAO
from service.contractService import ContractService
from service.computation_intern_strategy import ComputationInternStrategy
from service.computation_pro_strategy import ComputationProStrategy
from business_objects.league import League, LeagueModel
from business_objects.contract import Contract
from database.database import LeagueDB, ContractDB
from datetime import date,datetime
from service.utils import in_progress
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




    def add_league(self,league:LeagueModel) -> str : 
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
    
           

    def put_league_by_id(self, id: int, league: LeagueModel) -> Dict:
        dao = LeagueDAO()
        existing_league = dao.get_league_by_id(id)
        if existing_league:
            league_class = League(existing_league.name,existing_league.country,existing_league.level,
            existing_league.professional_minimum_wage,[existing_league.daily_salary_first_year,existing_league.daily_salary_second_year,existing_league.daily_salary_third_year]
            )
            
            all_contracts_dict = ContractService().get_all_contracts_by_id_league(id)
            for c in all_contracts_dict["contracts"]:
                if (c['date_end']>datetime.now().date()) : 
                    contract = Contract(salary=c["total_salary"],date_start=c["date_start"], date_end= c["date_end"])
                    contract.league = league_class
                    if c["type_contract"] == "professional":
                        contract.computation_strategy = ComputationProStrategy()
                    else : 
                        contract.computation_strategy = ComputationInternStrategy()
                    contract.update(league.professional_minimum_wage,league.internSalaryGrid)
                    ContractDAO().update_contract(c["id_contract"],contract.salary)
            LeagueDAO().put_league_by_id(existing_league,league)
            return {"message": f"The league with id {id} has been updated"}
        else:
            return {"message": f"The league with id {id} does not exist"}  


