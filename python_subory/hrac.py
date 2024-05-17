import random as ran
import pygame as pg

# moje importy
from panacik import Panacik

class Hrac: 
    def __init__(self, screen: pg.Surface, farba:str, coords:tuple,  n:int=4) -> None:
        self.n = n
        self.farba = farba
        self.screen = screen
        self.x, self.y = coords
        self.panacikovia = []
        self.kliknuty = None
        self.vytvor_panacikov()
        
    def vytvor_panacikov(self)->None:
        for i in range(self.n):
            self.panacikovia.append(Panacik(self.screen, self.x, self.y, self.farba))
            self.x += 40

    def hod_kockou(self) -> int:
        return ran.randint(1, 6)