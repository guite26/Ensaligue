from abc import ABC, abstractmethod
from business_objects.player import Player
from business_objects.league import League
from datetime import date
from typing import Optional

class AbstractComputationStrategy(ABC):

    @abstractmethod
    def compute_duration(player:Player,date_start:Optional[date] = None,duration:Optional[int] = None):
        return

    @abstractmethod
    def compute_end_date(self, date_start:date,duration:int):
        return 

    @abstractmethod
    def compute_salary(self, league: League,date_start:date, date_end:date, salary:Optional[int]=None):
        return 


