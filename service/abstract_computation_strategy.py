from abc import ABC, abstractmethod
from business_objects.player import Player
from business_objects.league import League
from datetime import date
from typing import Optional, List

class AbstractComputationStrategy(ABC):

    @abstractmethod
    def compute_duration(self,player_birth_date:date,date_start:Optional[date] = None,duration:Optional[int] = None):
        return

    @abstractmethod
    def compute_end_date(self, date_start:date,duration:int):
        return 

    @abstractmethod
    def compute_salary(self,min_salary:int,league_internal_salary_grid: List[float],date_start:date, date_end:date, salary:Optional[int]=None):
        return 
    

    @abstractmethod
    def update_salary(self,new_min_salary:int, new_league_internal_salary_grid: List[float],date_start:date, date_end : date,salary:int,internal_salary_grid : List[float]):
        return

