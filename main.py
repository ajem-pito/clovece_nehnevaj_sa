import pygame as pg
import random as ran

#moje importy
from panacik import Panacik

pg.init()

# konstanty
# to su nahodne cisla, ktore som si len tak vymyslel, casom ich mozme zmenit
SCREEN_WIDTH= 1000
SCREEN_HEIGHT = 800
FPS = 5

PANACIK_SIZE = (30, 60) #idkk nepamtam si presne velkost panacika

# farby RGB (red, green, blue)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Hrac:
    ...

class Hra():
    def __init__(self) -> None:
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        pg.display.set_caption("Clovece nehnevaj sa")
        self.running = True
        self.panacik = Panacik(self.screen, 300, 300, "red", 0, 30, 60)
        self.panacik_2 = Panacik(self.screen, 400, 300, "red", 0, 30, 60, 2)

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
            self.screen.blit(self.panacik.hover(pos), (self.panacik.x, self.panacik.y))
            self.screen.blit(self.panacik_2.hover(pos), (self.panacik_2.x, self.panacik_2.y))

            pg.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    hra = Hra()
    hra.game_loop()
