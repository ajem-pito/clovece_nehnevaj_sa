import pygame as pg

pg.init()

# konstanty
SIZE = (1000, 800)
FPS = 3
BG_FARBA = (102, 153, 204)

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Clovece nehnevaj sa")

clock = pg.time.Clock()

spritesheet = pg.image.load(r"panacik_sprites/cerveny panacik sprites.png").convert_alpha()

class Panacik:
    def __init__(self, farba:str = "red", frame:int = 0, width=30, height=60, scale:int=None) -> None:
        self.width = width
        self.height = height
        self.scale = scale
        self.frame = frame
        
        self.farba_panacik_dict = {
                      "red": r"panacik_sprites/cerveny panacik sprites.png", 
                      "green": r"", 
                      "blue": r"", 
                      "yellow": r"", 
                      "purple": r"", 
                      "orange": r"", 
                      "brown": r"", 
                      "pink": r""
                      }
        
        self.frame_dict = {
                      0:(0,0,30,60), 1:(31,0,61,60), 2:(61,0,94,60), 
                      3:(94,0,129,60), 4:(130,0,168,60), 5:(170,0,217,60), 
                      6:(219,0,273,60), 7:(275,0,312,60), 8:(315,0,361,60), 
                      9:(363,0,418,60), 10:(421,0,450,60), 11:(453,0,482,60), 
                      12:(484,0,512,60)
                      }
        
        self.sheet = pg.image.load(self.farba_panacik_dict[farba]).convert_alpha()

    def get_image(self) -> pg.Surface:
        sprite_suradnice: tuple = self.frame_dict[self.frame]
        width = sprite_suradnice[2] - sprite_suradnice[0]
        height = sprite_suradnice[3] - sprite_suradnice[1]
        image = pg.Surface((width, height)).convert_alpha()
        image.fill((0, 255, 250))
        image.blit(self.sheet, (0, 0), sprite_suradnice)
        if self.scale:
            image = pg.transform.scale(image, (self.width * self.scale, self.height * self.scale))
        image.set_colorkey((0, 255, 250))
        return image

panacik_0 = Panacik(frame=0).get_image()
panacik_1 = Panacik(frame=1).get_image()
panacik_2 = Panacik(frame=2).get_image()
panacik_3 = Panacik(frame=3).get_image()
panacik_4 = Panacik(frame=4).get_image()
panacik_5 = Panacik(frame=5).get_image()
panacik_6 = Panacik(frame=6).get_image()
panacik_7 = Panacik(frame=7).get_image()
panacik_8 = Panacik(frame=8).get_image()
panacik_9 = Panacik(frame=9).get_image()
panacik_10 = Panacik(frame=10, scale=4).get_image()
panacik_11 = Panacik(frame=11, scale=4).get_image()
panacik_12 = Panacik(frame=12).get_image()

run = True

glow = [panacik_10, panacik_11]
n = 0

while run:
    screen.fill(BG_FARBA)

    # screen.blit(spritesheet, (0, 0))

    screen.blit(glow[n], (0, 0))
    n = (n + 1) % 2
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
    clock.tick(FPS)
pg.quit()