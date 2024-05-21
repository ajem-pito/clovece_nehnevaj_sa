import pygame as pg

class Panacik:
    def __init__(self, screen:pg.Surface, x:int, y:int, farba:str = "red", frame:int = 0, width=30, height=60, scale:int=1) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale = scale
        self.frame = frame
        self.is_clicked_var = False
        self.pohyb_bool: bool = False # nie som si isty ci to je potreba ci niekedy pouzijem ale necham este
        self.poloha: int = 0
        self.timer = 0

        self.hover_var = 0
        self.idle_var = 0
        self.pohyb_var = 0

        self.farba_panacik_dict = {
                      "red": r"panacik_sprites/cerveny panacik sprites.png", 
                      "green": r"panacik_sprites/zeleny panacik sprites.png", 
                      "blue": r"panacik_sprites/modry panacik sprites.png", 
                      "yellow": r"panacik_sprites/zlty panacik sprites.png", 
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

        # v liste su framy, ktore sa maju zobrazia pri pohybe/nejakej aktivite
        self.normal = [0]
        self.pad_vlavo = [0,4,5,6]
        self.pad_vpravo = [0,7,8,9]
        self.pohyb_list = [0,4,5,6,5,4,0,7,8,9,8,7,0]
        self.idle_list = [0,1,2,3]
        self.glow = [10,11]
        self.smrt = [12]

        # if self.scale:
        #     self.width = self.width * self.scale
        #     self.height = self.height * self.scale
        #     print(self.width, self.height)

        # self.get_image()

    def get_image(self, frame = None) -> pg.Surface:
        if frame is not None:
            self.frame = frame
        sprite_suradnice: tuple = self.frame_dict[self.frame]
        width = sprite_suradnice[2] - sprite_suradnice[0]
        height = sprite_suradnice[3] - sprite_suradnice[1]
        self.image = pg.Surface((width, height)).convert_alpha()
        self.image.fill((0, 255, 250))
        self.image.blit(self.sheet, (0, 0), sprite_suradnice)
        if self.scale != 1:
            self.image = pg.transform.scale(self.image, (self.width * self.scale, self.height * self.scale))
        self.image.set_colorkey((0, 255, 250))
        return self.image
    
    def pohyb(self, pos) -> None:
        self.dx, self.dy = self.x - pos[0], self.y - pos[1]
        self.x += self.dx
        self.y += self.dy
        return self.get_image(self.pohyb_list[self.pohyb_var])

    def hover(self) -> pg.Surface:
        self.hover_var = (self.hover_var + 1) % 2
        return self.get_image(self.glow[self.hover_var])        

    def idle(self) -> None:
        self.idle_var = (self.idle_var + 1) % 4
        return self.get_image(self.idle_list[self.idle_var])



        