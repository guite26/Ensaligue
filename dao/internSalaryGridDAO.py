from database.database import InternSalaryGridDB, engine, session
from sqlalchemy.orm import Query
from typing import List

class internSalaryGridDAO():
    def __init__(self):
        pass

    def add_internSalaryGrid(self,internSalaryGrid:InternSalaryGridDB):
        # add it to the session and commit it
        session.add(internSalaryGrid)
        session.commit()
        # grab the id given to the object from the database
        id = internSalaryGrid.id_intern_salary_grid
        # close the session
        return id

    def get_internSalaryGrid_by_id(self,id:int) -> InternSalaryGridDB:
        # add it to the session and commit it
        internSalaryGriddb = session.get(entity=InternSalaryGridDB,ident=id)
        session.commit()
        return internSalaryGriddb

    def get_all_internSalaryGrid(self) -> List[InternSalaryGridDB] :
        # add it to the session and commit it
        all_internSalaryGrid = session.query(InternSalaryGridDB).all()
        return all_internSalaryGrid