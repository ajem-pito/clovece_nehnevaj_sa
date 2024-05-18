import pygame as pg
import random as rand
import os

# moje importy 
from test_hraci import Hrac, NPC
from panacik import Panacik

# inicializacia pygame
pg.init()

# konstanty - velkost okna
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900
# konstanty - farby
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

VELKOST = (30,60)
FPS = 60

# ... 
class Hra:
    def __init__(self, n_hracov: int) -> None:
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill(WHITE)
        pg.display.set_caption("Clovece nehnevaj sa")
        self.clock = pg.time.Clock()
        self.running = True

        self.hraci: list[object] = self.vytvor_hracov(n_hracov)
        self.mriezka: list[tuple[int, int]] = self.vytvor_mriezku()

        self.panacik = Panacik(self.screen, 0,0, "red")

    def vytvor_hracov(self, n) -> list[object]:
        list = []
        farba = ["red", "blue", "green", "yellow"]
        max = 4

        for id in range(max):
            if id <= n:
                list.append(Hrac(id))
            else: 
                list.append(NPC(id))

        # for hrac in list:
        #     print(hrac)

        return list
    
    def vytvor_mriezku(self) -> list:
        list = []
        
        for i in range(SCREEN_WIDTH // VELKOST[0] + 1):
            underlist = []
            for j in range(SCREEN_HEIGHT // VELKOST[1] + 1):
                underlist.append((i,j, None))

            list.append(underlist)

        # for riadok in list:
        #     print(riadok)
        
        return list

    def debug_mriezka(self) -> None:
        # pekna mriezka vznikne pri 1500 a 900
        for i in range(SCREEN_WIDTH // VELKOST[0]):
            pg.draw.line(self.screen, BLACK, (i*VELKOST[0],0), (i*VELKOST[0],SCREEN_HEIGHT), 2)
        
        for j in range(SCREEN_HEIGHT // VELKOST[1]):
            pg.draw.line(self.screen, BLACK, (0, j*VELKOST[1]), (SCREEN_WIDTH, j*VELKOST[1]), 2)

    def game_loop(self) -> None:
        while self.running:
            for hrac in self.hraci:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.running = False
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mys_pos = pg.mouse.get_pos()
                            if mys_pos:
                                print(hrac, mys_pos)
                            else:
                                continue

                self.screen.fill(WHITE)
                self.debug_mriezka()
                self.screen.blit(self.panacik.get_image(0), (20*30, 10*60))

                pg.display.flip()
                # pg.time.delay(100)
                self.clock.tick(FPS) 

if __name__ == "__main__":
    hra = Hra(n_hracov=3)
    hra.game_loop()
    pg.quit()