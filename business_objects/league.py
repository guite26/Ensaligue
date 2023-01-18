from pydantic.main import BaseModel
from typing import List

class League(BaseModel) : 
    name : str
    country : str
    level : int
    professional_minimum_wage : int
    internSalaryGrid : List[float]

