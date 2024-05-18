import random as ran
import pygame as pg

# moje importy
from panacik import Panacik

class Hrac: 
    def __init__(self, screen: pg.Surface, farba:str, coords:tuple = None,  n:int=4) -> None:
        self.n = n
        self.farba = farba
        self.screen = screen
        self.x, self.y = coords if coords else (0, 0)
        self.panacikovia = []
        self.kliknuty = None
        self.dict = {"red":(10,2), "blue": [(),(),(),()], "green":[(),(),(),()], "yellow":[(),(),(),()]}
        self.vytvor_panacikov()
        
    def vytvor_panacikov(self)->None:
        for i in range(self.n):
            self.panacikovia.append(Panacik(self.screen, self.x, self.y, self.farba))
            self.x += 54

        self.v_domceku = self.panacikovia

    def hod_kockou(self) -> int:
        return ran.randint(1, 6)