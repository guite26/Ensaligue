from dao.internSalaryGridDAO import internSalaryGridDAO

from business_objects.internSalaryGrid import InternSalaryGrid
from database.database import InternSalaryGridDB
from datetime import date
from typing import List, Dict

class InternSalaryGridService():
    def __init__(self):
        pass

    def is_valid_salary(self,daily_salary_first_year,daily_salary_seconde_year,daily_salary_third_year):
        try:

            # Compare salary
            if daily_salary_first_year < daily_salary_seconde_year & daily_salary_seconde_year < daily_salary_third_year :
                return True
            else:
                return False
        except ValueError:

            return False


    def add_internSalaryGrid(self,internSalaryGrid:InternSalaryGrid) -> str : 
        if not self.is_valid_salary(internSalaryGrid.daily_salary_first_year,internSalaryGrid.daily_salary_seconde_year,internSalaryGrid.daily_salary_third_year):
            return f"{internSalaryGrid.daily_salary_third_year} is not a valid salary"

        internSalaryGriddb = InternSalaryGridDB(daily_salary_first_year = internSalaryGrid.daily_salary_first_year, daily_salary_seconde_year = internSalaryGrid.daily_salary_seconde_year,daily_salary_third_year = internSalaryGrid.daily_salary_third_year )
        dao = internSalaryGridDAO()
        id = dao.add_internSalaryGrid(internSalaryGriddb)
        return f"created todo item with id {id}"


    def get_all_internSalaryGrid(self)-> List[Dict]:
        dao = internSalaryGridDAO()
        all_internSalaryGrid = dao.get_all_internSalaryGrid()
        res = {"internSalaryGrid": [internSalaryGrid.as_dict() for internSalaryGrid in all_internSalaryGrid]}
        return res

    def get_internSalaryGrid_by_id(self,id:int) -> InternSalaryGridDB:
        dao = internSalaryGridDAO()
        internSalaryGriddb = dao.get_internSalaryGrid_by_id(id)
        if internSalaryGriddb:
            return internSalaryGriddb.as_dict()
        else :
            return {"message":f'The internSalaryGrid with id {id} does not exist'}


    
            



    