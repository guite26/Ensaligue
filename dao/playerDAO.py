from database.database import PlayerDB, engine, session
from sqlalchemy.orm import Query
from typing import List
from business_objects.player import Player
from dao.utils_dao import updateobj
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
    
    def delete_player_by_id(self, id: int) -> PlayerDB:
        player = session.query(PlayerDB).get(id)
        if player:
            session.delete(player)
            session.commit()
        else:
            raise Exception("Player with id {} not found.".format(id))
   
    def put_player_by_id(self, existing_player : PlayerDB, new_player : Player) -> PlayerDB:
        existing_player.name = new_player.name
        existing_player.surname = new_player.surname
        existing_player.birth_date = new_player.birth_date
        existing_player.position = new_player.position
        session.commit()
        return existing_player
    



       