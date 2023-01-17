from pydantic.main import BaseModel

class InternSalaryGrid(BaseModel) :
    daily_salary_first_year : int
    daily_salary_seconde_year : int
    daily_salary_third_year : int
    