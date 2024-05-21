import pygame as pg
import random as rand

from test_panacik import Panacik
pg.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900
FPS = 60

class Menu:
    def __init__(self) -> None:
        self.running = True
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Clovece nehnevaj sa")
        self.clock = pg.time.Clock()
        self.panacikovia = []

        self.vytvor_texty()

    def vytvor_texty(self):
        text = "CLOVECE*NEHNEVAJ*SA*"
        font_velkost = 40
        font_path = r"font/ONESIZE.ttf"
        font = pg.font.Font(font_path, font_velkost)

        self.velkost_textu: tuple = font.size(text)
        image = font.render(text, True, (0,0,0))
        # text_rect: tuple[int,int,int,int] = image.get_rect(topleft=(x,y))
        
        # print(f"Text: {velkost_textu} Rect: {text_rect}")

        max_velkost = -self.velkost_textu[0]
        while max_velkost < SCREEN_WIDTH:
            max_velkost += self.velkost_textu[0]

        x,y = (-self.velkost_textu[0], 100)

        self.text = []
        for i in range(3):
            riadok = []
            for j in range(max_velkost//self.velkost_textu[0]+1):
                if i == 1:
                    riadok.append(Vytvor_text(self.screen, text, (x + j*self.velkost_textu[0],y + i * self.velkost_textu[1]), 
                                              font_velkost, max_velkost, font_path, 1, button=False, reverse=True))
                else:
                    riadok.append(Vytvor_text(self.screen, text, (x + j*self.velkost_textu[0],y + i * self.velkost_textu[1]),
                                              font_velkost, max_velkost, font_path, 1, button=False))
            self.text.append(riadok)

        # width = self.text[0][0].font.size(text)[0]
        # print(width)

        self.tlacidla = []
        self.texty = ["START", "SAVE", "NASTAVENIA"]
        for k in range(len(self.texty)):
            self.tlacidla.append(Vytvor_text(None, self.texty[k], (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + k*self.velkost_textu[1]), 30, 0, r"font/ONESIZE.ttf", 0, button=True))

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
                self.screen.blit(panacik.get_image(0), (panacik.x, panacik.y))
                panacik.update()
                    
            for riadok in self.text:
                for text in riadok:
                    image, rect = text.draw()
                    self.screen.blit(image, rect)
                    text.update()
            
            for tlacidlo in self.tlacidla:
                x,y = pg.mouse.get_pos()
                if x in range(tlacidlo.x - tlacidlo.velkost_textu[0], tlacidlo.x + tlacidlo.velkost_textu[0]) and y in range(tlacidlo.y - tlacidlo.velkost_textu[1]//2, tlacidlo.y + tlacidlo.velkost_textu[1]//2):
                    tlacidlo.text = '> ' + tlacidlo.origo_text + ' <'
                    tlacidlo.hover = True
                else:
                    tlacidlo.text = tlacidlo.origo_text
                    tlacidlo.hover = False
                image, rect = tlacidlo.draw()
                self.screen.blit(image, rect)

            pg.display.flip()
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

    def update(self) -> None:
        self.x += self.speed
        if self.x >= self.max_velkost:
            self.x = -self.velkost_textu[0]
        elif self.reverse and self.x <= -self.velkost_textu[0]:
            self.x = self.max_velkost


    def draw(self) -> tuple[pg.Surface, pg.Rect]:
        self.image = self.font.render(self.text, True, self.hover_farba if self.hover else self.farba)
        exec(f"{self.skuska[self.button]}") # obrovsky shoutout pre Alexa V. ze som toto unho videl
        return (self.image, self.rect)
    
    def on_click(self) -> None:
        pass

if __name__ == "__main__":
    menu = Menu()
    menu.menu_loop()

