from test_panacik import Panacik

meno_dict = {0: "Jano", 1: "Filip", 2: "Nina", 3: "Marek", 4: "Jakub"}

class Hrac:
    def __init__(self, id: int, farba: str, pos: tuple[int, int]):
        self.id = id
        self.farba = farba
        self.x, self.y = pos # pos == indexy x,y v mriezke
        self.kliknuty = None

        self.panacikovia = self.vytvor_panacikov(4)

    def __repr__(self) -> str:
        return f"{meno_dict[self.id]}"
    
    def vytvor_panacikov(self, n) -> list[object]:
        list = []
        for _ in range(n):
            list.append(Panacik(self.x, self.y, self.farba))
            self.x += 1
        return list

class NPC:
    def __init__(self, id, farba, pos: tuple[int, int]):
        self.id = id
        self.farba = farba
        self.x, self.y = pos # pos == indexy x,y v mriezke
        self.kliknuty = None

        self.panacikovia = self.vytvor_panacikov(4)

    def __repr__(self) -> str:
        return f"{meno_dict[self.id]}"
    
    def vytvor_panacikov(self, n) -> list[object]:
        list = []
        for _ in range(n):
            list.append(Panacik(self.x, self.y, self.farba))
            self.x += 1
        return list
