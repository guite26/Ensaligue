from database.database import LeagueDB, engine, session
from sqlalchemy.orm import Query
from typing import List

class LeagueDAO():
    def __init__(self):
        pass

    def add_league(self,league:LeagueDB):
        # add it to the session and commit it
        session.add(league)
        session.commit()
        # grab the id given to the object from the database
        id = league.id_league
        # close the session
        return id

    def get_league_by_id(self,id:int) -> LeagueDB:
        # add it to the session and commit it
        leaguedb = session.get(entity=LeagueDB,ident=id)
        session.commit()
        return leaguedb

    def get_all_leagues(self) -> List[LeagueDB] :
        # add it to the session and commit it
        all_leagues = session.query(LeagueDB).all()
        return all_leagues


    def delete_league_by_id(self,id:int):
        league = session.query(LeagueDB).filter_by(id_league=id).first()
        session.delete(league)
        session.commit()

    def put_league_by_id(self,id:int, league:LeagueDB):
        old_league = session.query(LeagueDB).filter_by(id_league=id).first()
        old_league.name = league.name
        old_league.country = league.country
        session.commit()