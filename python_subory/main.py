import pygame as pg
import random as ran

#moje importy
from panacik import Panacik
from hrac import Hrac
from menu import Menu
from mapa import Mapa

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
GRAY = (150, 150, 150)

class HracInterface:
    def __init__(self) -> None:
        ...

class Hra():
    def __init__(self) -> None:
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(pg.image.load("mapa01.png"), (0, 0))
        self.clock = pg.time.Clock()
        pg.display.set_caption("Clovece nehnevaj sa")
        self.running = True

        self.hraci = [
                      Hrac(self.screen,"red", (17, 2)),
                      Hrac(self.screen,"green", (995, 2)),
                      Hrac(self.screen,"blue", (17, 720)), 
                      Hrac(self.screen,"yellow", (995, 720))
                      ]
        
        self.mapa = Mapa()

    def hod_kockou_screen_func(self, hrac) -> None: # treba pozmenit nazov idkk
        self.hod_kockou_screen = ... #

    def game_loop(self) -> None:
        while self.running:
            
            self.screen.fill(GRAY)
            self.screen.blit(pg.image.load("mapa01.png"), (0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running  = False
            
            for hrac in self.hraci:
                for panacik in hrac.panacikovia:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            pos = pg.mouse.get_pos()
                            if (pos[0] in range(panacik.x, panacik.x + panacik.width * panacik.scale) and
                                pos[1] in range(panacik.y, panacik.y + panacik.height * panacik.scale)):
                                panacik.is_clicked_var = True if panacik.is_clicked_var == False else False
                                hrac.kliknuty = panacik if hrac.kliknuty == False else False
                                panacik.timer = 0

                    pos = pg.mouse.get_pos()
                    if (pos[0] in range(panacik.x, panacik.x + panacik.width * panacik.scale) and
                        pos[1] in range(panacik.y, panacik.y + panacik.height * panacik.scale)) or (panacik.is_clicked_var == True):
                        self.screen.blit(panacik.hover(), (panacik.x, panacik.y))

                    # elif panacik.is_clicked_var == True and pos[0] in range(SCREEN_WIDTH//2, SCREEN_WIDTH) and pos[1] in range(SCREEN_HEIGHT//2, SCREEN_HEIGHT):
                    #     self.screen.blit(panacik.pohyb(pos), (panacik.x, panacik.y))

                    elif panacik.timer > 3 and not panacik.is_clicked_var: #sekundy
                        self.screen.blit(panacik.idle(), (panacik.x, panacik.y))
                        
                    else:
                        self.screen.blit(panacik.get_image(0), (panacik.x, panacik.y))

                    panacik.timer += 0.1

            pg.display.flip() 
            pg.time.delay(80)

            self.clock.tick(FPS) # toto je uplna picovina, akoze na co to tu je, len to spomaluje program 😭😭😭

class Vytvor_Text:
    def __init__(self, screen: pg.Surface, text: str, font_size: int, position: tuple, text_color=(0,0,0), hover_color=(150, 150, 150), font_name=None, speed: float = 5) -> None:
        self.screen = screen
        self.text = text
        self.font = pg.font.Font(font_name, font_size)
        self.position = position
        self.text_color = text_color
        self.hover_color = hover_color
        self.speed = speed

        self.x, self.y = self.position
        self.draw(True)

    def draw(self, hover: bool = False) -> None:
        self.image = self.font.render(self.text, True, self.hover_color if hover else self.text_color)
        self.rect = self.image.get_rect(center=self.position)
        self.screen.blit(self.image, self.rect)

if __name__ == "__main__":
    hra = Hra()
    hra.game_loop()
