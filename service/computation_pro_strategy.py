from service.abstract_computation_strategy import AbstractComputationStrategy
from business_objects.player import Player
from business_objects.league import League

from service.utils import remaining_days
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
from typing import List

from service.exceptions import InvalidDurationException, InvalidSalaryException, InvalidAgeException

class ComputationProStrategy(AbstractComputationStrategy):

    def __init__(self) -> None:
        super().__init__()
    def compute_duration(self,player_birth_date: date, date_start: date,duration:int):
        if duration<1 :
            raise InvalidDurationException()
        elif player_birth_date > (datetime.now() + relativedelta(years=-16)).date() :
            raise InvalidAgeException()
        else :
            return duration 

    def compute_end_date(self, date_start:date,duration:int):
        date_end = date(date_start.year + duration -1 ,6,30) if date(date_start.year,6,30) > date_start else date(date_start.year + duration, 6,30)
        return date_end

    def compute_salary(self,min_salary:int, league_internal_salary_grid: List[float],date_start:date, date_end:int,salary:int):
        duration = ((date_end - date_start).days)//365  if date_start.day == 30 & date_start.month == 6 else ((date_end - date_start).days)//365
        if salary<min_salary:
            raise InvalidSalaryException()
        total_salary = salary * (((remaining_days(date_start))/365.25) + duration - 1)
        return total_salary
    
    def update_salary(self,new_min_salary:int, new_league_internal_salary_grid: List[float],date_start:date, date_end : date,salary:int,internal_salary_grid:List[float]):
        new_salary_hyp = self.compute_salary(new_min_salary, new_league_internal_salary_grid,date_start, date_end,new_min_salary)
        if new_salary_hyp>salary:
            date_update = datetime.now().date()
            new_total_salary = ((date_update - date_start)/(date_end - date_start))*salary + ((date_end - date_update)/(date_end - date_start))*new_salary_hyp
            return round(new_total_salary)
        else : 
            return salary

    