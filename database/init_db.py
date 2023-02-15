from sqlalchemy import create_engine, Column, Integer, String, Identity,MetaData, Sequence, ForeignKey, Date, Float
from sqlalchemy.engine.url import URL
from database.database import Base,engine, PlayerDB,TeamDB, LeagueDB, ContractDB,session
from sqlalchemy.ext.declarative import declarative_base
import os
from typing import List
from sqlalchemy.orm import Session
from datetime import date

def create_initial_data(session:Session):
    if session.query(PlayerDB).first():
        return
    # Define some functions to create and add initial records to the database
    players = [PlayerDB(name="Jean",surname="Dupond",birth_date=date(1990,1,1),position="ATT"),
    PlayerDB(name="Paul",surname="Dubois",birth_date=date(1990,1,1),position="DC"),
    PlayerDB(name="Theo",surname="Petit",birth_date=date(2004,4,1),position="MOC")]


    leagues  = [LeagueDB(name="Ligue 1", country="France",level=1,professional_minimum_wage=80000,daily_salary_first_year=20,daily_salary_second_year=30,daily_salary_third_year = 50),
    LeagueDB(name="Ligue 2", country="France",level=2,professional_minimum_wage=40000,daily_salary_first_year=15,daily_salary_second_year=25,daily_salary_third_year = 40)] 

    session.add_all(players)
    session.flush()
    session.add_all(leagues)
    session.flush()
    teams = [TeamDB(name="Rennes",id_league=1),TeamDB(name="Guingamp",id_league=2)]
    session.add_all(teams)
    session.flush()
    contracts = [ContractDB(id_player = 1,id_team=1,type_contract="professional",date_start=date(2023,2,15), date_end = date(2025,6,30),total_salary=1000000),
    ContractDB(id_player = 2,id_team=2,type_contract="professional",date_start=date(2023,2,15), date_end = date(2026,6,30),total_salary=200000),
    ContractDB(id_player = 3,id_team=2,type_contract="intern",date_start=date(2021,4,15), date_end = date(2023,6,30),total_salary=24880),
    ]
    session.add_all(contracts)
