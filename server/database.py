from sqlalchemy import create_engine, Column, Integer, String, Identity,MetaData, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///todooo.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Define To Do class inheriting from Base
class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(256))
    surnname = Column(String(256))
    team = Column(Integer,ForeignKey("team.id"))

class Team(Base):


class League(Base)