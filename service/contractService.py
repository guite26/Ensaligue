from dao.playerDAO import PlayerDAO
from dao.leagueDAO import LeagueDAO
from dao.teamDAO import TeamDAO
from dao.contractDAO import ContractDAO
from database.database import ContractDB, PlayerDB, TeamDB, LeagueDB
from typing import List, Dict

from business_objects.contract import Contract, ContractModel
from business_objects.player import Player
from business_objects.team import Team
from business_objects.league import League

from service.computation_intern_strategy import ComputationInternStrategy
from service.computation_pro_strategy import ComputationProStrategy
from service.teamService import TeamService

from datetime import datetime

class ContractService():

    def __init__(self) -> None:
        pass

    
    def add_contract(self,contract:ContractModel):
        player_db = PlayerDAO().get_player_by_id(contract.id_player)
        if not player_db:
            return {"message": f"The player id {contract.id_player} does not exist"}
        player = Player(name=player_db.name,surname=player_db.surname,birth_date=player_db.birth_date,position=player_db.position)
        team_db = TeamDAO().get_team_by_id(contract.id_team)
        if not team_db:
            return {"message": f"The team id {contract.id_team} does not exist"}
        league_db = LeagueDAO().get_league_by_id(team_db.id_league)
        league = League(name=league_db.name,country=league_db.country,
        professional_minimum_wage=league_db.professional_minimum_wage, level=league_db.level,
        internSalaryGrid=[league_db.daily_salary_first_year,league_db.daily_salary_second_year,league_db.daily_salary_third_year]
        )

        team = Team(name=team_db.name,league=league)
        contract_class = Contract(player=player,team=team,date_start=contract.date_start,duration=contract.duration,salary=contract.salary)

        if contract.type_contract == "professional":
            contract_class.computation_strategy = ComputationProStrategy()
        elif contract.type_contract == "intern":
            contract_class.computation_strategy = ComputationInternStrategy()
        
        contract_class.compute_duration()
        contract_class.compute_end_date()
        contract_class.compute_salary()

        contract_db = ContractDB(id_player=contract.id_player,id_team=contract.id_team,
        date_start=contract.date_start,date_end=contract_class.date_end,
        total_salary=contract_class.salary, type_contract=contract.type_contract)

        id = ContractDAO().add_contract(contract_db)
        return f"created contract with id {id}"
    
    def get_all_contracts_by_id_team(self,id_team)-> List[Dict]:
        dao = ContractDAO()
        all_contracts = dao.get_all_contracts_by_id_team(id_team)
        res = {"contracts": [contract.__dict__ for contract in all_contracts]}
        return res


    def get_all_contracts_by_id_league(self,id_league : int)-> List[Dict]:
        list_teams_in_league = TeamDAO().get_all_teams_by_id_league(id_league)
        dao = ContractDAO()
        list_contracts = []

        for team in list_teams_in_league :
            list_contracts.append(dao.get_all_contracts_by_id_team(team.id_team))

        res = {"contracts": [contract.__dict__ for l in list_contracts for contract in l]}

        return res

    def in_progress(self,contract : ContractDB) -> bool :
        return contract.date_end > datetime.now()
    
    def is_valide(self, contract : ContractDB) -> bool :
        pass