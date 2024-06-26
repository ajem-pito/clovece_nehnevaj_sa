from test_panacik import Panacik

meno_dict = {0: "Ego", 1: "Rytmus", 2: "Kuly", 3: "Fusino23"}
# mena = ["Jan", "Jozef", "Marek", "Peter", "Jana"]
farba = ["red", "blue", "green", "yellow"]
pos1 = [(1,3), (1,11), (16,3), (16,11)]

class Hrac:
    def __init__(self, id: int, farba: str, pos: tuple[int, int]):
        self.id = id
        self.farba = farba
        self.x, self.y = pos # pos == indexy x,y v mriezke
        self.kliknuty = None
        self.hody_kockou: list = []
        self.v_domceku = 0
        self.na_hracej_ploche = False
        self.n = 4

        self.panacikovia = self.vytvor_panacikov(4)

    def __repr__(self) -> str:
        return f"{meno_dict[self.id]}"
    
    def vytvor_panacikov(self, n) -> list[object]:
        list = []
        for _ in range(n):
            list.append(Panacik(self.x, self.y, self.farba))
            self.x += 1
        return list

class NPC(Hrac):
    def __init__(self, id, farba, pos: tuple[int, int]):
      super.__init__(id, farba, pos)