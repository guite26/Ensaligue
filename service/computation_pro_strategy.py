from service.abstract_computation_strategy import AbstractComputationStrategy
from business_objects.player import Player
from business_objects.league import League
from datetime import date, timedelta
from typing import List

class ComputationProStrategy(AbstractComputationStrategy):

    def __init__(self) -> None:
        super().__init__()
    def compute_duration(self,player_birth_date: date, date_start: date,duration:int):
        if duration<1 :
            raise ValueError("Le temps de contrat doit être de minimum 1 an.")
        else :
            return duration 

    def compute_end_date(self, date_start:date,duration:int):
        date_end = date(date_start.year + duration -1 ,6,30) if date(date_start.year,6,30) > date_start else date(date_start.year + duration, 6,30)
        return date_end

    def compute_salary(self, league_internal_salary_grid: List[float],date_start:date, duration:int,salary:int):
        total_salary = salary * duration
        return total_salary