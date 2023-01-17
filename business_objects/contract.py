from pydantic.main import BaseModel
from business_objects.team import Team
from datetime import date

class Contract(BaseModel):
    name : str
    surname : str
    team : Team 
    date_start : date
    duration = int
    salary = int
