from sqlalchemy import create_engine, Column, Integer, String, Identity,MetaData, Sequence, ForeignKey, Date
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()
print(os.environ.get('PORT'))
url_object = URL.create(
    drivername="postgresql+psycopg2",
    username=os.environ.get('USER'),
    password=os.environ.get('PASSWORD'),  # plain (unescaped) text
    host=os.environ.get('HOST_WEBSERVICE'),
    database=os.environ.get('DATABASE'),
    port=os.environ.get('PORT')
)
# Create a sqlite engine instance
engine = create_engine("sqlite:///ensaleague")
Session = sessionmaker(bind=engine)
print("ok")
# Create a DeclarativeMeta instance
Base = declarative_base()

# Define To Do class inheriting from Base
class Player(Base):
    __tablename__ = 'player'
    id_player = Column(Integer, Sequence("player_id_seq"), primary_key=True,nullable=False)
    name = Column(String(256),nullable=False)
    surnname = Column(String(256),nullable=False)
    birth_data = Column(Date,nullable=False)
    id_team = Column(Integer,ForeignKey("team.id_team"),nullable=False)

class Team(Base):
    __tablename__ = 'team'
    id_team = Column(Integer, Sequence("team_id_seq"), primary_key=True,nullable=False)
    name = Column(String(256),nullable=False)
    id_league = Column(String(256),ForeignKey("league.id_league"),nullable=False)

class League(Base):
    __tablename__ = 'league'
    id_league = Column(Integer, Sequence("league_id_seq"), primary_key=True,nullable=False)
    name = Column(String(256),nullable=False)
    country = Column(String(256),nullable=False)
    level = Column(Integer,nullable=False)
    id_inten_salary_grid = Column(Integer,ForeignKey("league.id_league"),nullable=False)
    professional_minimum_wage = Column(Integer,nullable=False)

class Contract(Base):
    __tablename__ = 'contract'
    id_contract = Column(Integer, Sequence("contract_id_seq"), primary_key=True,nullable=False)
    id_player = Column(String(256),ForeignKey("player.id_player"),nullable=False)
    id_team = Column(Integer,ForeignKey("team.id_team"))
    country = Column(String(256),nullable=False)
    date_start = Column(Date,nullable=False)
    date_end = Column(Date,nullable=False)
    total_salary = Column(Integer,nullable=False)
    type_contract = Column(String(256),nullable=False)

class InternSalaryGrid(Base):
    __tablename__ = 'intern_salary_grid'
    id_intern_salary_grid = Column(Integer, Sequence("id_intern_salary_grid_id_seq"), primary_key=True,nullable=False)
    daily_salary_first_year = Column(Integer,nullable=False)
    daily_salary_second_year = Column(Integer,nullable=False)
    daily_salary_third_year = Column(Integer,nullable=False)
print("ok2")
Base.metadata.create_all(engine)