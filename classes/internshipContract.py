from contract import Contract
from player import Player
from team import Team
from datetime import date


class InternContract(Contract):
    def __init__(self, player: Player, team: Team, date_start: date) -> None:
        super().__init__(player, team, date_start)
        duration = (self.player.birth_date.year+20) - self.date_start.year if (date(self.date_start.year,6,30)<self.date_start) else self.player.birth_date.year +20 -self.date_start.year +1
        if duration <= 0 :
            raise ValueError("Le joueuer est trop agé pour signer un contrat stagiaire")
        elif duration >=4 :
            raise ValueError("Le joueuer est trop jeune pour signer un contrat stagiaire")
        else :
            self.duration = duration
            self.end_date = date(self.date_start.year + self.duration -1 ,6,30) if date(self.date_start.year,6,30) > self.date_start else date(self.date_start.year+ self.duration, 6,30)

        self.salary = sum(x*y for x,y in zip([0 if i < ((3-duration) %3) else (date(self.date_start.year,6,30)-self.date_start).days if (self.date_start<date(self.date_start.year,6,30)) else (date(self.date_start.year+1,6,30)-self.date_start).days if i == ((3-duration) %3) else 365 for i in range(3)], [self.team.league.internSalaryGrid.daily_salary_first_year,self.team.league.internSalaryGrid.daily_salary_second_year,self.team.league.internSalaryGrid.daily_salary_thrid_year]))