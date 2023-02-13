from sqlalchemy import create_engine, Column, Integer, String, Identity,MetaData, Sequence, ForeignKey, Date, Float
from sqlalchemy.engine.url import URL
from database.database import Base,engine
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy.orm import Session
print("ENGINE",engine)
print(os.getenv("DATABASE_URL"))
Base.metadata.create_all(engine)