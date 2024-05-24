import random as rand

class Logika:
    def __init__(self, mapa) -> None:
        self.mapa: list[tuple[int,int]] = []
        self.domceky= {"red":[],
                       "blue":[],
                       "green":[],
                       "yellow":[]}
        
    def hod_kockou(self, hrac) -> int:
        return rand.randint(1,6)
        
    def pohyb(self) -> bool:
        pass

    def vyhodit(self) -> bool:
        pass
    
    def domcek(self) -> bool:
        pass

    def koniec(self) -> bool:
        pass