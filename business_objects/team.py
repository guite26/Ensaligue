from pydantic.main import BaseModel
import business_objects.league as league_bo
from business_objects.league_subscriber import LeagueSubscriber

from typing import List

class TeamModel(BaseModel) : 
    name : str
    id_league : int

class Team :
    def __init__(self,name : str,league : league_bo.League) -> None:
        self.name = name
        self.league = league
        self._subscribers : List[LeagueSubscriber] = []

    @property
    def subscribers(self):
        return self._subscribers

    @subscribers.setter
    def subscribers(self,subscribers):
        self._subscribers = subscribers

    def notify(self):
        pass