import pygame as pg
import random as rand
# import os

# moje importy 
from test_hraci import Hrac, NPC
from test_panacik import Panacik
from test_logika import Logika

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
        pg.display.set_caption("Clovece nehnevaj sa")
        self.clock = pg.time.Clock()
        self.running = True

        self.background_map = pg.image.load("mapa01.png").convert_alpha()
        # self.cerveny_panacik = pg.image.load(r"panacik_sprites/cerveny_hrac.ase")

        self.hraci: list[object] = self.vytvor_hracov(n_hracov)
        self.mriezka: list[tuple[int, int]] = self.vytvor_mriezku()

        self.logika = Logika(self.mriezka)
        self.cas = Cas()

    def vytvor_hracov(self, n) -> list[object]:
        self.hrac_n = 0
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
            
            self.screen.fill(WHITE)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            
            self.screen.blit(self.background_map, (0,0))
            # self.screen.blit(self.cerveny_panacik, (120,120), area=(0,0,120,120))

            # for hrac in self.hraci:
            #     for panacik in hrac.panacikovia:
            #         panacik.timer += 0.1
            #         self.screen.blit(panacik.get_image(0), (self.panacik.x, self.panacik.y))
                    
            # for panacik in self.hraci[self.hrac_n].panacikovia:
            #     for event in pg.event.get():
            #         if event.type == pg.QUIT:
            #             self.running = False
            #         elif event.type == pg.MOUSEBUTTONDOWN:
            #             if event.button == 1:
            #                 mys_pos = pg.mouse.get_pos()
            #                 x = mys_pos[0] // VELKOST[0] // 2 
            #                 y = mys_pos[1] // VELKOST[1]
            #                 # self.panacik.x = x*VELKOST[0] * 2 + 15
            #                 # self.panacik.y = y*VELKOST[1]
            #                 self.hrac_n = (self.hrac_n + 1) % 4
            #                 print(f"X: {x}, Y: {y}")
            for hrac in self.hraci:
                for panacik in hrac.panacikovia:
                    x = panacik.x * 60 + 15
                    y = panacik.y * 60  
                    
                    if panacik.rect.collidepoint(pg.mouse.get_pos()) or panacik.is_clicked_var == True:
                        self.screen.blit(panacik.hover(), (x, y))
                    
                    elif panacik.timer > 3:
                        self.screen.blit(panacik.idle(), (x, y))

                    else:
                        self.screen.blit(panacik.get_image(0), (x, y))
                    
                    panacik.timer += 1

            # self.debug_mriezka()

            self.cas.update()
            image, rect = self.cas.text.draw()
            self.screen.blit(image, rect)

            pg.display.flip()
            pg.time.delay(80)
            self.clock.tick(FPS) 

class Vytvor_text:
    def __init__(self, screen: pg.Surface, text: str, pos: tuple[int, int], font_velkost: int, max_velkost: int, font_path: str = None, speed: float = 1,
                 farba: tuple[int, int, int] = (0,0,0), hover_farba:tuple[int, int, int] = (255,0,0), reverse: bool = False, button: bool = False) -> None:
        self.screen = screen
        self.text, self.origo_text = text, text
        self.x, self.y = pos
        self.max_velkost: int = max_velkost
        self.font = pg.font.Font(font_path, font_velkost)
        self.velkost_textu:tuple[int, int] = self.font.size(text)
        self.speed = speed if not reverse else -speed
        self.farba = farba
        self.hover_farba = hover_farba
        self.reverse = reverse
        self.button = button
        self.hover = False
        self.skuska = ["self.rect = self.image.get_rect(topleft=(self.x, self.y))",
                       "self.rect = self.image.get_rect(center=(self.x, self.y))"]
        
        self.image = self.font.render(self.text, True, self.hover_farba if self.hover else self.farba)
        exec(f"{self.skuska[self.button]}")
    
    def update(self) -> None:
        self.x += self.speed
        if self.x >= self.max_velkost:
            self.x = -self.velkost_textu[0]
        elif self.reverse and self.x <= -self.velkost_textu[0]:
            self.x = self.max_velkost

    def draw(self) -> tuple[pg.Surface, pg.Rect]:
        self.image = self.font.render(self.text, True, self.hover_farba if self.hover else self.farba)
        exec(f"{self.skuska[self.button]}") # obrovsky shoutout pre Alexa V. ze som toto unho videl # aj ked ALex V je cisty frajer, je to picovina jak mraky
        return (self.image, self.rect)
    
    def on_click(self, mys_pos) -> None:
        return self.rect.collidepoint(mys_pos) 

class Cas:
    def __init__(self) -> None:
        self.text = Vytvor_text(screen=None, text="0:0", pos=(0,0), font_velkost=40, max_velkost=0, font_path=r"font/ONESIZE.ttf", speed=1,
                                farba=(255,255,255), hover_farba=(255,0,0), reverse=False, button=False)
        
        self.velkost_textu: tuple[int, int] = self.text.velkost_textu
        self.text.x = 11*60 - self.velkost_textu[0]
        self.text.y = 10
        self.sekundy = 0
        self.minuty = 0

    def update(self) -> None:
        cas = pg.time.get_ticks()
        self.sekundy = cas // 1000
        
        if self.sekundy // 60 >= 1:
            self.minuty += 1
            

        self.sekundy = self.sekundy % 60

        self.text.text = f"{self.minuty}:{self.sekundy}"




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
