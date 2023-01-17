from player import Player
from team import Team
from datetime import date, datetime
from abc import ABC, abstractmethod
class Contract(ABC) :
    def __init__(self,player : Player,team : Team,date_start : date,duration:int=None,salary:int=None) -> None:
        self.player = player
        self.team = team
        self.date_start = date_start
        self.duration = duration
        self.salary = salary
    
    @property
    def salary(self):
        return self.salary

    @property
    def end_date(self):
        return self.end_date