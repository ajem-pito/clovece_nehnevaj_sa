import pygame as pg
import random as rand
# import os

# moje importy 
from test_hraci import Hrac, NPC
from test_panacik import Panacik
from test_logika import Logika, Hod_kockou

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
YELLOW = (255, 255, 0)

ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)


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
        self.ego = pg.image.load(r"obrazky/ego.png").convert_alpha()
        self.rytmus = pg.image.load(r"obrazky/rytmus.png").convert_alpha()
        self.kuly = pg.image.load(r"obrazky/kuly.png").convert_alpha()
        self.fusino = pg.image.load(r"obrazky/fusino.png").convert_alpha()

        # self.cerveny_panacik = pg.image.load(r"panacik_sprites/cerveny_hrac.ase")

        self.hraci: list[object] = self.vytvor_hracov(n_hracov)
        self.mriezka: list[tuple[int, int]] = self.vytvor_mriezku()
        self.vytvor_UI()

        self.logika = Logika(self.mriezka)
        self.cas = Cas()

    def vytvor_UI(self) -> None:
        self.UI_list = []
        texty = ["HRAC NA RADE:", "1", "HOD KOCKOU", "STATUS:", "Index out of range"]
        pozicie = [(23*60, 20), (23*60, 70), (23*60, 3*60), (23*60, 6*60), (23*60, 6*60+20)]
        font_velkosti = [22, 50, 30, 22, 22]
        farby = [(0,0,0), (0,0,0), (0,0,0), (0,0,0), ORANGE]
        buttons = [True, True, True, True, True]

        for text, pos, font_velkost, farba , button in zip(texty, pozicie, font_velkosti, farby, buttons):
            self.UI_list.append(Vytvor_text(screen=None, text=text, pos=pos, font_velkost=font_velkost, max_velkost=0, font_path=r"font/ONESIZE.ttf", speed=1,
                                            farba=farba, hover_farba=(255,0,0), reverse=False, button=button))

        # self.hrac_na_rade_text = Vytvor_text(screen=None, text="HRAC NA RADE:", pos=(0,0), font_velkost=22, max_velkost=0, font_path=r"font/ONESIZE.ttf", speed=1,
        #                                 farba=(0,0,0), hover_farba=(255,0,0), reverse=False, button=False)
        # self.hrac_na_rade_text2 = Vytvor_text(screen=None, text="1", pos=(0,0), font_velkost=50, max_velkost=0, font_path=r"font/ONESIZE.ttf", speed=1,
        #                                 farba=(0,0,0), hover_farba=(255,0,0), reverse=False, button=False)
        # self.hod_kockou_button = Vytvor_text(screen=None, text="HOD KOCKOU", pos=(0,0), font_velkost=30, max_velkost=0, font_path=r"font/ONESIZE.ttf", speed=1,
        #                                      farba=(0,0,0), hover_farba=(255,0,0), reverse=False, button=True)
        # self.sprava_text = Vytvor_text(screen=None, text="STATUS:", pos=(0,0), font_velkost=22, max_velkost=0, font_path=r"font/ONESIZE.ttf", speed=1,
        #                                farba=(0,0,0), hover_farba=(255,0,0), reverse=False, button=False)
        
        # self.hrac_na_rade_text.x = 22*60 - 15
        # self.hrac_na_rade_text.y = 20

        # self.hrac_na_rade_text2.x = 22*60
        # self.hrac_na_rade_text2.y = 40

        # self.hod_kockou_button.x = 23*60
        # self.hod_kockou_button.y = 3*60

        # self.sprava_text.x = 22*60 + 15
        # self.sprava_text.y = 6*60
        
        # self.UI_list = [self.hrac_na_rade_text, self.hrac_na_rade_text2, self.hod_kockou_button, self.sprava_text]

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

        return list
    
    def vytvor_mriezku(self) -> list[list[tuple[int, int]]]:
        list = []
        
        for i in range(SCREEN_WIDTH // VELKOST[0] // 2): # riadok
            underlist = []
            for j in range(0, SCREEN_HEIGHT // VELKOST[1]): # stlpec
                underlist.append((i,j, None))
            list.append(underlist)
        
        return list

    def debug_mriezka(self) -> None:
        # pekna mriezka vznikne pri 1500 a 900
        for i in range(0, SCREEN_WIDTH // VELKOST[0], 2): # vertikalne
            pg.draw.line(self.screen, BLACK, (i*VELKOST[0],0), (i*VELKOST[0],SCREEN_HEIGHT), 2)
        
        for j in range(SCREEN_HEIGHT // VELKOST[1]): # horizontalne
            pg.draw.line(self.screen, BLACK, (0, j*VELKOST[1]), (SCREEN_WIDTH, j*VELKOST[1]), 2)

    def game_loop(self) -> None:
        hod_kockou_var = Hod_kockou()
        n = 1
        hrac_na_rade = next(iter(self.hraci)) # obrovsky shouout pre niekoho ze som toto videl edit: strasna picovina, nech sa dotycni zabije
        n2 = 0

        while self.running:
            self.screen.fill((128, 128, 128))
            self.screen.blit(self.background_map, (0,0))
            self.screen.blit(self.ego, (120,60))
            self.screen.blit(self.rytmus, (120,730))
            self.screen.blit(self.kuly, (1020,60))
            self.screen.blit(self.fusino, (1020,730))
            
            # cas
            self.cas.update()
            image, rect = self.cas.text.draw()
            self.screen.blit(image, rect)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.UI_list[2].on_click(pg.mouse.get_pos()):
                            n = self.logika.hod_kockou(self.hraci[self.hrac_n])
                            n2 = (n2 + 1) % 4

            self.screen.blit(hod_kockou_var.return_image(n), (22*60,3*60+30))

            hrac_na_rade = self.hraci[n2]
            self.UI_list[1].text = f"{hrac_na_rade}"
            self.UI_list[1].farba = hrac_na_rade.farba.upper()
            for text in self.UI_list:
                if self.UI_list[2].rect.collidepoint(pg.mouse.get_pos()):
                    self.UI_list[2].text = '> ' + self.UI_list[2].origo_text + ' <'
                    self.UI_list[2].hover = True
                else:
                    self.UI_list[2].text = self.UI_list[2].origo_text
                    self.UI_list[2].hover = False

                image, rect = text.draw()
                self.screen.blit(image, rect)

            # vykreslenie panacikov hraca ktory je na rade
            for panacik in hrac_na_rade.panacikovia:
                x = panacik.x * 60 + 15
                y = panacik.y * 60

                if panacik.rect.collidepoint(pg.mouse.get_pos()) or panacik.is_clicked_var == True:
                    self.screen.blit(panacik.hover(), (x, y))
                
                # if event.type == pg.MOUSEBUTTONDOWN:
                #     if event.button == 1:
                #         if panacik.rect.collidepoint(pg.mouse.get_pos()):
                #             panacik.is_clicked_var = True if not panacik.is_clicked_var else False
                #             hrac_na_rade.kliknuty = panacik if panacik.is_clicked_var else None
                #             continue

                elif panacik.is_clicked_var:
                    self.screen.blit(panacik.hover(), (x, y))

                else:
                    self.screen.blit(panacik.idle(), (x, y))


            # sluzi asi len na to, aby sa kazdy panacik, okrem toho co je na rade, zobrazil
            for hrac in self.hraci:
                if hrac.id != hrac_na_rade.id:
                    for panacik in hrac.panacikovia:
                        x = panacik.x * 60 + 15
                        y = panacik.y * 60  
                        self.screen.blit(panacik.get_image(0), (x, y))
                        
            # debugy
            # self.debug_mriezka()

            # update a ticky
            pg.display.flip()
            self.clock.tick(15) 

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
        sekundy = cas // 1000
        minuty = sekundy // 60
        sekundy %= 60
        self.text.text = f"{minuty}:{sekundy:02}"

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
