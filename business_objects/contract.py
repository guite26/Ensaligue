from pydantic.main import BaseModel
from business_objects.team import Team
from datetime import date
from typing import Union

from player import Player
from team import Team
from datetime import date, datetime
from abc import ABC, abstractmethod

from service.computeSalaryStrategy import ComputeSalaryStrategy

class ContractModel(BaseModel):
    id_player : int
    id_team : int 
    date_start : date
    duration = int
    salary : Union[int,None] = None

    
class Contract() :
    def __init__(self,player : Player,team : Team,date_start : date,duration:int=None,salary:int=None) -> None:
        self.player = player
        self.team = team
        self.date_start = date_start
        self.duration = duration
        self.salary = salary
        self._compute_salary_strategy : ComputeSalaryStrategy
    
    @property
    def salary(self):
        return self.salary

    @property
    def end_date(self):
        return self.end_date
    @property
    def compute_salary_strategy(self):
        return self._compute_salary_strategy
    
    @compute_salary_strategy.setter
    def compute_salary_strategy(self,compute_salary_strategy:ComputeSalaryStrategy):
        self._compute_salary_strategy = compute_salary_strategy
    
    def compute_salary(self):
        self._compute_salary_strategy.compute_salary(self.player,self.team.league,self.date_start,self.end_date, self.salary)
