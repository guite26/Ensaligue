from pydantic.main import BaseModel
from business_objects.league import League

class Team(BaseModel) : 
    name : str
    id_league : int
    