from dao.playerDAO import PlayerDAO
from business_objects.player import Player
from database.database import PlayerDB
from datetime import date
from typing import List, Dict

class PlayerService():
    def __init__(self):
        pass

    def is_valid_birthdate(self,birthdate):
        try:
            # Convert birthdate string to datetime object
            birthdate = birthdate
            # Compare birthdate to current date
            if birthdate < date.today():
                return True
            else:
                return False
        except ValueError:
            # Return False if birthdate is not in the correct format
            return False

    def is_valid_position(self,position):
        pass

    def is_existing_player(self,player:Player) -> bool:
        pass


    def add_player(self,player:Player) -> str : 
        if not self.is_valid_birthdate(player.birth_date):
            return f"{player.birth_date} is not a valid birthdate"
        playerdb = PlayerDB(name = player.name,surname=player.surname,birth_date=player.birth_date,position=player.position)
        dao = PlayerDAO()
        id = dao.add_player(playerdb)
        return f"created player with id {id}"

    def get_all_players(self)-> List[Dict]:
        dao = PlayerDAO()
        all_players = dao.get_all_players()
        res = {"players": [player.as_dict() for player in all_players]}
        return res

    def get_player_by_id(self,id:int) -> Dict:
        dao = PlayerDAO()
        playerdb = dao.get_player_by_id(id)
        if playerdb:
            return playerdb.as_dict()
        else :
            return {"message":f'The player with id {id} does not exist'}

    def delete_player_by_id(self, id: int) -> Dict:
        dao = PlayerDAO()
        player = dao.get_player_by_id(id)
        if player:
            dao.delete_player_by_id(id)
            return {"message": f"The player with id {id} has been deleted"}
        else:
            return {"message": f"The player with id {id} does not exist"}
  
    def put_player_by_id(self, id: int, player: Player) -> Dict:
        dao = PlayerDAO()
        existing_player = dao.get_player_by_id(id)
        if existing_player:
            if not self.is_valid_birthdate(player.birth_date):
                return {"message": f"{player.birth_date} is not a valid birthdate"}
            dao.put_player_by_id(existing_player,player)
            return {"message": f"The player with id {id} has been updated"}
        else:
            return {"message": f"The player with id {id} does not exist"}    
            