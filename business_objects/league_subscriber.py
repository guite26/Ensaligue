from abc import ABC,abstractmethod

class LeagueSubscriber(ABC):

    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod 
    def update(self,context):
        pass
