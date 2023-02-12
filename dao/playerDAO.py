from database.database import PlayerDB, engine, session
from sqlalchemy.orm import Query
from typing import List

class PlayerDAO():
    def __init__(self):
        pass

    def add_player(self,player:PlayerDB):
        # add it to the session and commit it
        session.add(player)
        session.commit()
        # grab the id given to the object from the database
        id = player.id_player
        # close the session
        return id

    def get_player_by_id(self,id:int) -> PlayerDB:
        # add it to the session and commit it
        playerdb = session.get(entity=PlayerDB,ident=id)
        session.commit()
        return playerdb

    def get_all_players(self) -> List[PlayerDB] :
        # add it to the session and commit it
        all_players = session.query(PlayerDB).all()
        return all_players
        