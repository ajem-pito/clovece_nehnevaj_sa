import pygame as pg
import random as ran

pg.init()

SCREEN_WIDTH= 1400
SCREEN_HEIGHT = 800
FPS = 60


class Menu:
    def __init__(self) -> None:
        self.running = True
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((200, 248, 255))
        
        self.text = " Clovece nehnevaj sa"
        self.font_size = 40
        self.text_l = pg.font.Font(None, self.font_size).size(self.text)[0]
        self.hustota = SCREEN_WIDTH // self.text_l
        print(self.hustota, len(self.text))

        # text_length, text_height = font.size(text_content)

        self.clock = pg.time.Clock()
        pg.display.set_caption("Clovece nehnevaj sa")

        self.nadpisi_1 = []
        self.nadpisi_2 = []
        self.nadpisi_3 = []

        self.vytvor_text()

    def vytvor_text(self) -> None:
        # pre 1. riadok
        for i in range(self.hustota+2):
            self.nadpisi_1.append(VytvorText2(self.screen, self.text, 40, (i*self.text_l, 100), font_name=None, speed=5))
        
        # pre 2. riadok
        for i in range(self.hustota+2):
            self.nadpisi_2.append(VytvorText2(self.screen, self.text, 40, (i*self.text_l, 140), font_name=None, speed=5))
        
        # pre 3. riadok
        for i in range(self.hustota+2):
            self.nadpisi_3.append(VytvorText2(self.screen, self.text, 40, (i*self.text_l, 180), font_name=None, speed=5))
        
    def menu_loop(self) -> None:
        while self.running:
            self.screen.fill((200, 248, 255))
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pg.mouse.get_pos()
                        print("kliknutie", pos)

            for nadpis1 in self.nadpisi_1:
                nadpis1.update()
                nadpis1.draw(False)
            
            for nadpis2 in self.nadpisi_2:
                nadpis2.update(True)
                nadpis2.draw(False)

            for nadpis3 in self.nadpisi_3:
                nadpis3.update()
                nadpis3.draw(False)
                
            pg.display.flip()
            self.clock.tick(60)

class VytvorText2:
    def __init__(self, screen: pg.Surface, text: str, font_size: int, position: tuple, text_color=(0,0,0), hover_color=(150, 150, 150), font_name=None, speed: float = 5) -> None:
        self.screen = screen
        self.text = text
        self.font = pg.font.Font(font_name, font_size)
        self.position = position
        self.text_color = text_color
        self.hover_color = hover_color
        self.speed = speed

        self.x, self.y = self.position
        self.draw(False)
    
    def draw(self, hover: bool) -> None:
        self.image = self.font.render(self.text, True, self.hover_color if hover else self.text_color)
        self.rect = self.image.get_rect(center=self.position)
        self.screen.blit(self.image, self.rect)
    
    def update(self, reverse: bool = False) -> None:
        self.x += self.speed if not reverse else -self.speed
        if self.x > SCREEN_WIDTH and not reverse:
            self.x = 0-self.rect.width
            self.position = (self.x, self.y)
        elif self.x < 0-self.rect.width and reverse:
            self.x = SCREEN_WIDTH+self.rect.width
            self.position = (self.x, self.y)
        
        else:
            if reverse:
                self.x -= self.speed
            else:
                self.x += self.speed
            self.position = (self.x, self.y)
    
if __name__ == "__main__":
    menu = Menu()
    menu.menu_loop()
    

# import pygame as pg

# pg.init()

# SCREEN_WIDTH = 1400
# SCREEN_HEIGHT = 800
# FPS = 60

# class Menu:
#     def __init__(self):
#         self.running = True
#         self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#         self.screen.fill((200, 248, 255))

#         self.text = " Clovece nehnevaj sa"
#         self.font_size = 40
#         self.text_width = pg.font.Font(None, self.font_size).size(self.text)[0]
#         self.spacing = SCREEN_WIDTH // self.text_width

#         self.clock = pg.time.Clock()
#         pg.display.set_caption("Clovece nehnevaj sa")

#         self.lines = [[] for _ in range(3)]
#         self.create_text()

#     def create_text(self):
#         for i in range(self.spacing + 2):
#             for j in range(3):
#                 self.lines[j].append(Text(self.screen, self.text, 40, (i * self.text_width, 100 + j * 40), font_name=None, speed=5))

#     def menu_loop(self):
#         while self.running:
#             self.screen.fill((200, 248, 255))
#             for event in pg.event.get():
#                 if event.type == pg.QUIT:
#                     self.running = False

#             for line in self.lines:
#                 for text_obj in line:
#                     text_obj.update()
#                     text_obj.draw(False)

#             pg.display.flip()
#             self.clock.tick(60)

# class Text:
#     def __init__(self, screen, text, font_size, position, text_color=(0, 0, 0), hover_color=(150, 150, 150), font_name=None, speed=5):
#         self.screen = screen
#         self.text = text
#         self.font = pg.font.Font(font_name, font_size)
#         self.position = position
#         self.text_color = text_color
#         self.hover_color = hover_color
#         self.speed = speed

#         self.x, self.y = self.position
#         self.draw(False)

#     def draw(self, hover):
#         self.image = self.font.render(self.text, True, self.hover_color if hover else self.text_color)
#         self.rect = self.image.get_rect(center=self.position)
#         self.screen.blit(self.image, self.rect)

#     def update(self, reverse=False):
#         self.x += self.speed if not reverse else -self.speed
#         if self.x > SCREEN_WIDTH and not reverse:
#             self.x = 0 - self.rect.width
#             self.position = (self.x, self.y)
#         elif self.x < 0 - self.rect.width and reverse:
#             self.x = SCREEN_WIDTH + self.rect.width
#             self.position = (self.x, self.y)
#         else:
#             if reverse:
#                 self.x -= self.speed
#             else:
#                 self.x += self.speed
#             self.position = (self.x, self.y)

# if __name__ == "__main__":
#     menu = Menu()
#     menu.menu_loop()
#     pg.quit()
