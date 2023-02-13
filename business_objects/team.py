from pydantic.main import BaseModel
import business_objects.league as league_bo

class TeamModel(BaseModel) : 
    name : str
    id_league : int

class Team :
    def __init__(self,name : str,league : league_bo.League) -> None:
        self.name = name
        self.league = league
    