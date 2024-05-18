from panacik import Panacik

meno_dict = {0: "Jano", 1: "Filip", 2: "Nina", 3: "Marek", 4: "Jakub"}

class Hrac:
    def __init__(self, id: int):
        self.id = id
    
    # def __str__(self) -> str:
    #     return f"{meno_dict[self.id]}"
    
    def __repr__(self) -> str:
        return f"{meno_dict[self.id]}"

class NPC:
    def __init__(self, id, farba ):
        self.id = id
        self.farba = farba

    # def __str__(self) -> str:
    #     return f"{meno_dict[self.meno]}"
    
    def __repr__(self) -> str:
        return f"{meno_dict[self.id]}"
    
    def vytvor_panacikov(self, n) -> list[object]:
        list = []
        max = 4

        for id in range(max):
            if id <= n:
                list.append(Hrac(id))
            else: 
                list.append(NPC(id))

        # for hrac in list:
        #     print(hrac)

        return list
