from datetime import date
class Player :
    def __init__(self,name : str,surname : str,birth_date:date,positon : str) -> None:
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.position = positon
        