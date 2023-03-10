from service.abstract_computation_strategy import AbstractComputationStrategy
from datetime import date,datetime
from typing import Optional, List
from service.exceptions import InvalidAgeOldException, InvalidAgeYoungException, InvalidDurationException

from service.utils import new_total_salary, get_days_periods
class ComputationInternStrategy(AbstractComputationStrategy):

    def __init__(self) -> None:
        super().__init__()
    
    def compute_duration(self,player_birth_date: date, date_start: Optional[date] = None, duration: Optional[int] = None):
        duration = (player_birth_date.year+19) - date_start.year if (date(date_start.year,6,30)<date_start) else player_birth_date.year +19 -date_start.year +1
        if duration <= 0 :
            raise InvalidAgeOldException()
        elif duration >=4 :
            raise InvalidAgeYoungException()
        else :
            return duration
            
    def compute_end_date(self, date_start:date,duration:int):
        if duration<1 :
            raise InvalidDurationException()
        else :
            date_end = date(date_start.year + duration -1 ,6,30) if date(date_start.year,6,30) > date_start else date(date_start.year + duration, 6,30)
        return date_end

    def compute_salary(self, min_salary:int,league_internal_salary_grid: List[float],date_start:date, date_end:date,salary:int=None):
        days_per_season = get_days_periods(date_start,date_end)
        total_salary = sum(x*y for x, y in zip(days_per_season, league_internal_salary_grid))
        
        return total_salary

    def update_salary(self,new_min_salary, new_league_internal_salary_grid,date_start, date_end,salary,internal_salary_grid):
        date_update = datetime.now().date()
        if date_update<date_start :
            new_tot_salary = self.compute_salary(new_min_salary,new_league_internal_salary_grid,date_start,date_end,salary)
        else : 
            new_tot_salary= new_total_salary(date_start,date_end,internal_salary_grid,new_league_internal_salary_grid)
        return new_tot_salary
