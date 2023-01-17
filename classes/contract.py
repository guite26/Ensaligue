from player import Player
from team import Team
from datetime import date

class Contract :
    def __init__(self,player : Player,team : Team,date_start : date,date_end : date,salary : int) -> None:
        self.player = player
        self.team = team
        self.date_start = date_start
        self.date_end = date_end
        self.salary = salary
