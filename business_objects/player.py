from datetime import date
from pydantic.main import BaseModel

class Player(BaseModel) : 
    name : str
    surname : str
    birth_date : date
    position : str
