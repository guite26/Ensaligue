from pydantic.main import BaseModel
from business_objects.league import League

class TeamModel(BaseModel) : 
    name : str
    id_league : int

class Team :
    def __init__(self,name : str,league : League) -> None:
        self.name = name
        self.league = league
    