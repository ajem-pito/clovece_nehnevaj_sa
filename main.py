import pygame as pg
import random as ran

#moje importy
from panacik import Panacik
from hrac import Hrac
from menu import Menu

pg.init()

# konstanty
# to su nahodne cisla, ktore som si len tak vymyslel, casom ich mozme zmenit
SCREEN_WIDTH= 1400
SCREEN_HEIGHT = 800
FPS = 60

PANACIK_SIZE = (30, 60) # x, y 
PANACIK_SCALE = 1

# farby RGB (red, green, blue)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Hra():
    def __init__(self) -> None:
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        pg.display.set_caption("Clovece nehnevaj sa")
        self.running = True

        self.hraci = [
                      Hrac(self.screen,"red", (100, 100)),
                      Hrac(self.screen,"green", (100, 200)),
                      Hrac(self.screen,"blue", (100, 300)), 
                      Hrac(self.screen,"yellow", (100, 400))
                      ]

    def hod_kockou_screen(self, hrac) -> None: # treba pozmenit nazov idkk
        self.hod_kockou_screen = ...

    def game_loop(self) -> None:
        while self.running:
            
            self.screen.fill((102,153,204))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running  = False

                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pg.mouse.get_pos()
                        print("kliknutie", pos)
            
            pos = pg.mouse.get_pos()
            
            for hrac in self.hraci:
                for panacik in hrac.panacikovia:
                    self.screen.blit(panacik.hover(pos), (panacik.x, panacik.y))
        
            pg.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    hra = Hra()
    hra.game_loop()
