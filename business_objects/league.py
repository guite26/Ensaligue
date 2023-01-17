from pydantic.main import BaseModel
from business_objects.internSalaryGrid import InternSalaryGrid

class League(BaseModel) : 
    name : str
    country : str
    level : int
    professional_minimum_wage : int
    internSalaryGrid : InternSalaryGrid

