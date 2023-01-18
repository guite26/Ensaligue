from sqlalchemy import create_engine, Column, Integer, String, Identity,MetaData, Sequence, ForeignKey, Date, Float
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from typing import Dict
load_dotenv()
url_object = URL.create(
    drivername="postgresql+psycopg2",
    username=os.environ.get('USER'),
    password=os.environ.get('PASSWORD'),  # plain (unescaped) text
    host=os.environ.get('HOST_WEBSERVICE'),
    database=os.environ.get('DATABASE'),
    port=os.environ.get('PORT')
)
# Create a sqlite engine instance
engine = create_engine("sqlite:///ensaleague.db")
session = Session(bind=engine)
# Create a DeclarativeMeta instance
Base = declarative_base()

# Define To Do class inheriting from Base
class PlayerDB(Base):
    __tablename__ = 'player'
    id_player = Column(Integer, Sequence("player_id_seq"), primary_key=True,nullable=False)
    name = Column(String(256),nullable=False)
    surname = Column(String(256),nullable=False)
    birth_date = Column(Date,nullable=False)
    position = Column(String(256),nullable=False)

    def as_dict(self) -> Dict:
        dict_repr = {
            "id_player" : self.id_player,
            "name" : self.name,
            "surname" : self.surname,
            "birth_date" : self.birth_date,
            "position" : self.position
        }
        return dict_repr
    
class TeamDB(Base):
    __tablename__ = 'team'
    id_team = Column(Integer, Sequence("team_id_seq"), primary_key=True,nullable=False)
    name = Column(String(256),nullable=False)
    id_league = Column(String(256),ForeignKey("league.id_league"),nullable=False)

class LeagueDB(Base):
    __tablename__ = 'league'
    id_league = Column(Integer, Sequence("league_id_seq"), primary_key=True,nullable=False)
    name = Column(String(256),nullable=False)
    country = Column(String(256),nullable=False)
    level = Column(Integer,nullable=False)
    professional_minimum_wage = Column(Integer,nullable=False)
    daily_salary_first_year = Column(Float,nullable=False)
    daily_salary_second_year = Column(Float,nullable=False)
    daily_salary_third_year = Column(Float,nullable=False)

class ContractDB(Base):
    __tablename__ = 'contract'
    id_contract = Column(Integer, Sequence("contract_id_seq"), primary_key=True,nullable=False)
    id_player = Column(String(256),ForeignKey("player.id_player"),nullable=False)
    id_team = Column(Integer,ForeignKey("team.id_team"),nullable=False)
    country = Column(String(256),nullable=False)
    date_start = Column(Date,nullable=False)
    date_end = Column(Date,nullable=False)
    total_salary = Column(Integer,nullable=False)
    type_contract = Column(String(256),nullable=False)


Base.metadata.create_all(engine)