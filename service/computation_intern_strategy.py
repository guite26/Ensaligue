from typing import Optional, List
from service.exceptions import InvalidAgeOldException, InvalidAgeYoungException, InvalidDurationException
from datetime import date
from service.abstract_computation_strategy import AbstractComputationStrategy

class ComputationInternStrategy(AbstractComputationStrategy):

    def __init__(self) -> None:
        super().__init__()
    
    def compute_duration(self,player_birth_date: date, date_start: Optional[date] = None, duration: Optional[int] = None):
        duration = (player_birth_date.year+20) - date_start.year if (date(date_start.year,6,30)<date_start) else player_birth_date.year +20 -date_start.year +1
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

    def compute_salary(self, min_salary:int,league_internal_salary_grid: List[float],date_start:date, duration:int,salary:int=None):
        days_per_season = [
            0 if i < ((3-duration) %3) else 
            (date(date_start.year, 6, 30) - date_start).days if date_start < date(date_start.year, 6, 30) else 
            (date(date_start.year+1, 6, 30) - date_start).days if i == ((3-duration) %3) else 365 
            for i in range(3)
        ]
        total_salary = sum(x*y for x, y in zip(days_per_season, league_internal_salary_grid))
        
        return total_salary