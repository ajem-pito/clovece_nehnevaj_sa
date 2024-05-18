import pygame as pg
import random as rand
# import os

# moje importy 
from test_hraci import Hrac, NPC
from test_panacik import Panacik

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

        self.background_map = pg.image.load("mapa01.png")
        # self.cerveny_panacik = pg.image.load(r"panacik_sprites/cerveny_hrac.ase")

        self.hraci: list[object] = self.vytvor_hracov(n_hracov)
        self.mriezka: list[tuple[int, int]] = self.vytvor_mriezku()

        self.panacik = Panacik(0, 0)

    def vytvor_hracov(self, n) -> list[object]:
        list = []
        farba = ["red", "blue", "green", "yellow"]
        pos = [(1,3), (1,11), (16,3), (16,11)]
        max = 4

        for id in range(max):
            if id <= n:
                list.append(Hrac(id, farba[id], pos[id]))
            else: 
                list.append(NPC(id, farba[id], pos[id]))

        # for hrac in list:
        #     print(hrac)

        return list
    
    def vytvor_mriezku(self) -> list[list[tuple[int, int]]]:
        list = []
        
        for i in range(SCREEN_WIDTH // VELKOST[0] // 2): # riadok
            underlist = []
            for j in range(0, SCREEN_HEIGHT // VELKOST[1]): # stlpec
                underlist.append((i,j, None))
            list.append(underlist)

        # for riadok in list:
        #     print(riadok)
        
        return list

    def debug_mriezka(self) -> None:
        # pekna mriezka vznikne pri 1500 a 900
        for i in range(0, SCREEN_WIDTH // VELKOST[0], 2): # vertikalne
            pg.draw.line(self.screen, BLACK, (i*VELKOST[0],0), (i*VELKOST[0],SCREEN_HEIGHT), 2)
        
        for j in range(SCREEN_HEIGHT // VELKOST[1]): # horizontalne
            pg.draw.line(self.screen, BLACK, (0, j*VELKOST[1]), (SCREEN_WIDTH, j*VELKOST[1]), 2)

    def game_loop(self) -> None:
        while self.running:
            
            self.screen.fill(BLACK)
            self.screen.blit(self.background_map, (0,0))
            # self.screen.blit(self.cerveny_panacik, (120,120), area=(0,0,120,120))

            for hrac in self.hraci:
                for panacik in hrac.panacikovia:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            self.running = False
                        elif event.type == pg.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                mys_pos = pg.mouse.get_pos()
                                x = mys_pos[0] // VELKOST[0] // 2 
                                y = mys_pos[1] // VELKOST[1]
                                self.panacik.x = x*VELKOST[0] * 2 + 15
                                self.panacik.y = y*VELKOST[1]

                    x = panacik.x * 60 + 15
                    y = panacik.y*60  
                    
                    mys_pos = pg.mouse.get_pos()

                    if (mys_pos[0] in range(x, x + panacik.width * panacik.scale) and
                        mys_pos[1] in range(y, y + panacik.height * panacik.scale)) or (panacik.is_clicked_var == True):
                        self.screen.blit(panacik.hover(), (x, y))
                    
                    elif panacik.timer > 3:
                        self.screen.blit(panacik.idle(), (x, y))

                    else:
                        self.screen.blit(panacik.get_image(0), (x, y))

                    panacik.timer += 0.1

                    self.screen.blit(self.panacik.get_image(0), (self.panacik.x, self.panacik.y))

            # self.debug_mriezka()

            pg.display.flip()
            pg.time.delay(80)
            self.clock.tick(FPS) 

if __name__ == "__main__":
    hra = Hra(n_hracov=3)
    hra.game_loop()
    pg.quit()


# vysvetlivky == mriezka
# self.mriezka[riadok][stlpec][0] == x
# self.mriezka[riadok][stlpec][1] == y

# print(self.mriezka[0][8])
# x = self.mriezka[0][8][0]*VELKOST[0]
# y = self.mriezka[0][8][1]*VELKOST[1]


# pg.draw.circle(self.screen, BLACK, (self.panacik.x , self.panacik.y), 15, 60) # 2 == hrubka
