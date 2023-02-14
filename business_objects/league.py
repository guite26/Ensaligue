from pydantic.main import BaseModel
from typing import List, Union
from business_objects.league_subscriber import LeagueSubscriber

class LeagueModel(BaseModel) : 
    name : str
    country : str
    level : int
    professional_minimum_wage : int
    internSalaryGrid : List[float]


class League():
    def __init__(self,name:str,country:str,level:int,professional_minimum_wage:int,internSalaryGrid:List[float]) -> None:
        self.name = name
        self.country = country
        self.level = level
        self.professional_minimum_wage = professional_minimum_wage
        self.internSalaryGrid = internSalaryGrid
        self._subscribers : List[LeagueSubscriber] = []
    
    @property
    def subscribers(self):
        return self._subscribers

    @subscribers.setter
    def subscribers(self,subscribers):
        self._subscribers = subscribers

    def notify(self):
        if not self._subscribers:
            return 
        for s in self._subscribers:
            s.update(self)