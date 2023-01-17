from contract import Contract
from player import Player
from team import Team
from datetime import date

class InternContract(Contract):

    def __init__(self, player: Player, team: Team, date_start: date) -> None:
        super().__init__(player, team, date_start)
        duration = (self.player.birth_date.year+20) - self.date_start.year if (date(self.date_start.year,6,30)<self.date_start) else self.player.birth_date.year +20 -self.date_start.year +1
        if duration <= 0 :
            raise ValueError("le joueuer est trop agé pour signer un contrat stagiaire")
        elif duration >=4:
            raise ValueError("le joueuer est trop jeune pour signer un contrat stagiaire")
        else :
            self.duration = duration
        
        
         
