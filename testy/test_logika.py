import pygame as pg
import random as rand

class Logika:
    def __init__(self, mapa) -> None:
        self.mapa: list[tuple[int,int]] = [
            (1,5, None), (3,5), (5,5), (7,5), (7,4), (7,3), (7,2), (7,1), (9,1), (11,1), (13,1), (13,2),
            (13,3, None), (13,4), (13,5), (15,5), (17,5), (19,5), (19,6), (19,7), (19,8), (19,9), (17,9),
            (15,9, None), (13,9), (13,10), (13,11), (13,12), (13,13), (11,13), (9,13), (7,13), (7,12), (7,13),
            (7,12, None), (7,11), (7,10), (7,9), (5,9), (3,9), (1,9), (1,8), (1,7), (1,6)
        ]
        self.domceky= {
            "red":[(3,7, None), (4, 7, None), (5, 7, None), (6, 7, None)],
            "blue":[(10,8, None), (10,9, None), (10,10, None), (10,11, None)],
            "green":[(10,3, None), (10,4, None), (10,5, None), (10,6, None)],
            "yellow":[(14, 7, None), (15, 7, None), (16, 7, None), (17, 7, None)]
        }
        
    def hod_kockou(self, hrac) -> int:
        return rand.randint(1,6)
        
    def pohyb(self, panacik, n) -> bool:
        pass

    def vyhodit(self, panacik, n) -> bool:
        pass
    
    def domcek(self, n) -> bool:
        pass

    def koniec(self) -> bool:
        pass

class Hod_kockou:
    def __init__(self, scale=1) -> None:
        self.sheet = pg.image.load(r"kocka_sprite.png").convert_alpha()
        self.frame_dict = {1:(0,0,129,130), 2:(130,0,256,130), 3:(258,0,384,130),
                           4:(385,0,510,130), 5:(510,0,638,130), 6:(638,0,770,130)}
        
        # self.frame = 1
        self.scale = scale
        self.x = 0 
        self.y = 0

    def return_image(self, frame = None) -> None:
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
        # self.rect = self.image.get_rect(topleft=(self.x*60+15, self.y*60))
        return self.image
    
    # idk
    def rolling_animation(self):
        ...
    

# najprv sa vyberie hrac na rade
# musi hodit kockou, ak nema este panacika na mape hadze sa kocka 4krat
# ak ma panacika na mape hadze sa kocka 1krat
# ak hadze 6ku, moze si vybrat ci chce vytiahnut panacika z domceka a hadze znova kockou
# ak hodi kockou a ma panacika na mape musi sa pohnut o hodnotu kocky
# ak sa pohne na policko, kde je panacik, vyhodi sa von
# ak vsetko prebehne v poriadku, ide dalej hrac na rade

# def hra():
#     logika = Logika(mapa)
#     hrac_na_rade = "red"  # predpokladam, ze zacina hrac "red"
    
#     while not logika.koniec():
#         # vyberie sa hrac na rade
#         hrac = logika.domceky[hrac_na_rade]
        
#         # musi hodit kockou, ak nema este panacika na mape hadze sa kocka 4krat
#         # ak ma panacika na mape hadze sa kocka 1krat
#         pocet_hodov = 4 if len(hrac) == 0 else 1
        
#         for _ in range(pocet_hodov):
#             hod = logika.hod_kockou(hrac)
            
#             # ak hadze 6ku, moze si vybrat ci chce vytiahnut panacika z domceka a hadze znova kockou
#             if hod == 6:
#                 if logika.domcek():
#                     continue
            
#             # ak hodi kockou a ma panacika na mape musi sa pohnut o hodnotu kocky
#             if len(hrac) > 0:
#                 if not logika.pohyb(hod):
#                     continue
            
#             # ak sa pohne na policko, kde je panacik, vyhodi sa von
#             if logika.vyhodit():
#                 continue
        
#         # ak vsetko prebehne v poriadku, ide dalej hrac na rade
#         hrac_na_rade = next(iter(logika.domceky.keys()))