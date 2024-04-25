import pygame as pg
# import random

pg.init()

# konstanty
# to su nahodne cisla, ktore som si len tak vymyslel, casom ich mozme zmenit
SCREEN_WIDTH= 1000
SCREEN_HEIGHT = 800
FPS = 5

# farby RGB (red, green, blue)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# viem, ze existuje pg.sprite.Sprite, ale nechcel som to pouzit, 
# lebo som si chcel vyskusat vlastne veci, neskor mozme pouzit
class Pohybujuci_panacik():
    def __init__(self) -> None:
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.n = 0
        self.idk()

    def idk(self):
        self.spites: list = ["./panacik_sprites/panacik_sprite_0.png",
                             "./panacik_sprites/panacik_sprite_1.png",
                             "./panacik_sprites/panacik_sprite_2.png"]
        
        self.load_spites: list = []
        for i in self.spites:
            self.load_spites.append(pg.image.load(i))

    def draw(self, screen):
        screen.blit(self.load_spites[self.n], (self.x, self.y))
        self.n = (self.n + 1) % 3
        

class Hra(Pohybujuci_panacik):
    def __init__(self) -> None:
        Pohybujuci_panacik.__init__(self)
        self.running = True

    def game_run(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("panacik gameplay")
        self.clock = pg.time.Clock()
        while self.running:
            self.screen.fill(WHITE)
            self.draw(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.clock.tick(FPS)
            pg.display.flip()

if __name__ == "__main__":
    hra = Hra()
    hra.game_run()