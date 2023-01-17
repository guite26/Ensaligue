from contract import Contract
from player import Player
from team import Team
from datetime import date

class ProfessionalContract(Contract) :
    def __init__(self, player: Player, team: Team, date_start: date,duration : int, salary:int) -> None:
        super().__init__(player, team, date_start)

        if duration<1 :
            raise ValueError("Le temps de contrat doit être de minimum 1 an.")
        else :
            self.duration = duration
            self.date_end = date(self.date_start.year + self.duration -1 ,6,30) if date(self.date_start.year,6,30) > self.date_start else date(self.date_start.year+ self.duration, 6,30)
        
        if salary<self.team.league.professional_minimum_wage :
            raise ValueError("Le salaire indiqué est inferieur au salaire minimum dans cette ligue.")
        else :
            self.salary = salary