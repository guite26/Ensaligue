from InternSalaryGrid import InternSalaryGrid
class League :
    def __init__(self,name : str,country : str,level : int,internSalaryGrid : InternSalaryGrid,professional_minimum_wage : int) -> None:
        self.name = name
        self.country = country
        self.level = level
        self.internSalaryGrid = internSalaryGrid
        self.professional_minimum_wage = professional_minimum_wage