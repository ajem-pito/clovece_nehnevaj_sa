import pygame as pg
import random as rand

from test_panacik import Panacik
pg.init()

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
FPS = 60

class Menu:
    def __init__(self) -> None:
        self.running = True
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Clovece nehnevaj sa")
        self.clock = pg.time.Clock()
        self.panacikovia = []

        self.vytvor_text()

    def vytvor_text(self):
        text = "CLOVECE*NEHNEVAJ*SA*"
        x,y = (0, 100)
        font_velkost = 40
        font_path = r"font/ONESIZE.ttf"
        # font_path = r"font/Arcade.ttf"
        # font_path = None
        font = pg.font.Font(font_path, font_velkost)
        velkost_textu: tuple = font.size(text)
        # self.text: list[list[object]] = [[Vytvor_text(self.screen, text, (pos[0], pos[1] + x*80), font_velkost, font_path) for y in range(SCREEN_WIDTH // font.size(text)[0])] for x in range(3)]
        
        self.text = []
        for i in range(3):
            riadok  = []
            for j in range(SCREEN_WIDTH // velkost_textu[0] + 1):
                if i == 1:
                    riadok.append(Vytvor_text(self.screen, text, (x+j*velkost_textu[0],y+i*velkost_textu[1]), font_velkost, font_path, reverse=True))
                else:
                    riadok.append(Vytvor_text(self.screen, text, (x+j*velkost_textu[0],y+i*velkost_textu[1]), font_velkost, font_path))
            self.text.append(riadok)

        # width = self.text[0][0].font.size(text)[0]
        # print(width)

        self.start = Vytvor_text(self.screen, "START", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2), 30, font_path, button=True)
        self.save = Vytvor_text(self.screen, "SAVE", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2 + velkost_textu[1]), 30, font_path, button=True)
        self.nastavenia = Vytvor_text(self.screen, "NASTAVENIA", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2 + velkost_textu[1]*2), 30, font_path, button=True)
        

    def background_panacik(self) -> None:
        # if rand.randint(0,100) > 50:
        x = rand.randint(200, SCREEN_WIDTH+600)
        y = -60            
            
        farba = rand.choice(["red", "green", "blue", "yellow"])
        self.panacikovia.append(Panacik(x,y,farba,1, scale=1, speed=3))

    def menu_loop(self):
        while self.running:
            self.screen.fill((255,255,255))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            
            if rand.randint(0,100) < 5:
                self.background_panacik()

            for panacik in self.panacikovia:
                panacik.update()
                self.screen.blit(panacik.get_image(), (panacik.x, panacik.y))
                    
            for line in self.text:
                for text in line:
                    text.update()
                    image, rect = text.draw()
                    self.screen.blit(image, rect)

            jo = self.start.draw()
            self.screen.blit(jo[0], jo[1])
            jo = self.save.draw()
            self.screen.blit(jo[0], jo[1])
            jo = self.nastavenia.draw()
            self.screen.blit(jo[0], jo[1])

            pg.display.flip()

            self.clock.tick(FPS)


class Vytvor_text:
    def __init__(self, screen: pg.Surface, text: str, pos: tuple[int, int], font_velkost: int, font_path: str = None, speed: float = 1,
                 farba: tuple[int, int, int] = (0,0,0), hover_farba:tuple[int, int, int] = (255,0,0), reverse: bool = False, button: bool = False) -> None:
        self.screen = screen
        self.text = text
        self.x, self.y = pos
        self.font = pg.font.Font(font_path, font_velkost)
        self.velkost_text:tuple[int, int] = self.font.size(text)
        self.speed = speed if not reverse else -speed
        self.farba = farba
        self.hover_farba = hover_farba
        self.reverse = reverse
        self.button = button

        self.skuska = ["self.rect = self.image.get_rect(topleft=(self.x, self.y))",
                       "self.rect = self.image.get_rect(center=(self.x, self.y))"]

    def update(self) -> None:
        self.x += self.speed
        if self.x > SCREEN_WIDTH and not self.reverse:
            self.x = 0 - self.velkost_text[0]
        elif self.x < 0 - self.velkost_text[0] and self.reverse:
            self.x = SCREEN_WIDTH + self.velkost_text[0]

    def draw(self, hover: bool = False) -> tuple[pg.Surface, pg.Rect]:
        self.image = self.font.render(self.text, True, self.hover_farba if hover else self.farba)
        exec(f"{self.skuska[self.button]}") # obrovsky shoutout pre Alexa V. ze som toto unho videl
        return (self.image, self.rect)
    
    def on_click(self) -> None:
        pass

if __name__ == "__main__":
    menu = Menu()
    menu.menu_loop()

