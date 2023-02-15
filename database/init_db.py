from sqlalchemy import create_engine, Column, Integer, String, Identity,MetaData, Sequence, ForeignKey, Date, Float
from sqlalchemy.engine.url import URL
from database.database import Base,engine, PlayerDB,TeamDB, LeagueDB, ContractDB
from sqlalchemy.ext.declarative import declarative_base
import os
from typing import List
from sqlalchemy.orm import Session
def create_initial_data(session):
    # Define some functions to create and add initial records to the database
    players : List[PlayerDB] = [PlayerDB()]
    model2 = Model2(name="Example Model 2")
    model3 = Model3(name="Example Model 3")

    session.add(model1)
    session.add(model2)
    session.add(model3)

if __name__ == "__main__":
    engine = create_engine("postgresql://user:password@db:5432/dbname")  # Replace with your own database connection details
    Model.metadata.create_all(engine)

    # If you want to insert some initial data, create a session and call your functions
    with Session(engine) as session:
        create_initial_data(session)
        session.commit()