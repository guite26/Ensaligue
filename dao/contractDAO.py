from database.database import ContractDB, engine, session
from sqlalchemy.orm import Query
from typing import List
from datetime import datetime
class ContractDAO():
    def __init__(self):
        pass

    def add_contract(self,contract:ContractDB):
        # add it to the session and commit it
        session.add(contract)
        session.commit()
        # grab the id given to the object from the database
        id = contract.id_contract
        # close the session
        return id

    def get_contract_by_id(self,id:int) -> ContractDB:
        # add it to the session and commit it
        contractdb = session.get(entity=ContractDB,ident=id)
        return contractdb

    def get_all_contracts(self) -> List[ContractDB] :
        # add it to the session and commit it
        all_contracts = session.query(ContractDB).all()
        return all_contracts
    
    def get_all_contracts_by_id_team(self, id_team: int) -> List[ContractDB]:
        contractdb = session.query(ContractDB).filter_by(id_team = id_team).all()
        return contractdb
    
    def stop_contract(self,existing_contract : ContractDB) :
        existing_contract.date_end = datetime.now()
        session.commit()
        return existing_contract

    

