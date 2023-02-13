from pydantic.main import BaseModel
from datetime import date, datetime
from abc import ABC, abstractmethod

from datetime import date
from typing import Union, Literal

from business_objects.player import Player
import business_objects.team as team_bo
from business_objects.league_subscriber import LeagueSubscriber


from service.abstract_computation_strategy import AbstractComputationStrategy

class ContractModel(BaseModel):
    id_player : int
    id_team : int 
    date_start : date
    duration : Union[int,None] = None
    salary : Union[int,None] = None
    type_contract : Literal['professional','intern']
   
class Contract() :
    def __init__(self,player : Player,team : team_bo.Team,date_start : date,duration:int=None,salary:int=None) -> None:
        self.player = player
        self.team = team
        self.date_start = date_start
        self.duration = duration
        self.salary = salary
        self._computation_strategy : AbstractComputationStrategy
    
    @property
    def computation_strategy(self):
        return self._computation_strategy
    
    @computation_strategy.setter
    def computation_strategy(self,computation_strategy:AbstractComputationStrategy):
        self._computation_strategy = computation_strategy
    
    def compute_duration(self):
        self.duration = self._computation_strategy.compute_duration(self.player.birth_date,self.date_start,self.duration)

    def compute_end_date(self):
        self.date_end = self._computation_strategy.compute_end_date(self.date_start,self.duration)

    def compute_salary(self):
        self.salary = self._computation_strategy.compute_salary(self.team.league.internSalaryGrid,self.date_start,self.duration,self.salary)
    
    def update_league(self,new_internSalaryGrid):
        self.salary = self.compute_salary(new_internSalaryGrid,self.date_start,self.duration,self.salary)