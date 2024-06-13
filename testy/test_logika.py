import pygame as pg
import random as rand

class Logika:
    def __init__(self, mapa) -> None:
        self.mapa: list[tuple[int,int, str]] = [
            (1, 5, None), (3, 5, None), (5, 5, None), (7, 5, None), (7, 4, None), (7, 3, None), (7, 2, None), (7, 1, None), 
            (9, 1, None), (11, 1, None), (13, 1, None), (13, 2, None), (13, 3, None), (13, 4, None), (13, 5, None), (15, 5, None),
            (17, 5, None), (19, 5, None), (19, 6, None), (19, 7, None), (19, 8, None), (19, 9, None), (17, 9, None), (15, 9, None),
            (13, 9, None), (13, 10, None), (13, 11, None), (13, 12, None), (13, 13, None), (11, 13, None), (9, 13, None), (7, 13, None),
            (7, 12, None), (7, 13, None), (7, 12, None), (7, 11, None), (7, 10, None), (7, 9, None), (5, 9, None), (3, 9, None), (1, 9, None),
            (1, 8, None), (1, 7, None), (1, 6, None)
        ]
        
        self.domceky= {
            "red":[(3,7, None), (4, 7, None), (5, 7, None), (6, 7, None)],
            "blue":[(10,11, None), (10,10, None), (10, 9, None), (10, 8, None)],
            "green":[(10,3, None), (10,4, None), (10,5, None), (10,6, None)],
            "yellow":[(14, 7, None), (15, 7, None), (16, 7, None), (17, 7, None)]
        }

        self.starty = {
            "red":(1, 5, None), "blue":(7, 13, None), "green":(13, 1, None), "yellow":(19, 9, None)
        }
    
        # cesta panacika spociva z self.mapa + self.domceky

    def hod_kockou(self):
        return rand.randint(1, 6)

    def pohyb(self, hrac, panacik, pocet_krokov):
        if panacik.pos + pocet_krokov >= len(panacik.cesta):
            return False
        

        # if self.mapa[panacik.cesta[panacik.pos + pocet_krokov]] is not None:
        #     if self.vyhodit(hrac, panacik):
        #         return False

        panacik.pos += pocet_krokov
        panacik.x, panacik.y = panacik.cesta[panacik.pos][:2]

    def vyhodit(self, hrac, panacik):
        for hrac in self.hraci:
            for panacik in hrac.panacikovia:
                if panacik.x == panacik.x and panacik.y == panacik.y and panacik not in hrac.panacikovia:
                    panacik.poloha = 0
                    panacik.x, panacik.y = hrac.pos
                    return True
        return False
    
    # ak hadze 6ku, moze si vybrat ci chce vytiahnut panacika a hadze znova kockou
    def vyber_panacika(self, hrac, panacik):
        if self.starty[hrac.farba] not in self.mapa:
            return False
        
        pos = self.starty[hrac.farba]
        panacik.x = pos[0]
        panacik.y = pos[1]
        panacik.cesta = self.vytvor_cestu((pos[0], pos[1], None), hrac.farba)
        panacik.pos = panacik.cesta.index((pos[0], pos[1], None))
        self.mapa[self.mapa.index(pos)] = (pos[0], pos[1], panacik.id)
        panacik.na_hracie_ploche = True
        return True

    def koniec(self, hrac):
        if hrac.v_domceku == 4:
            return True
        return False
    
    def vytvor_cestu(self, start, farba) -> list:
        index_of_start = self.mapa.index(start)
        after_start = self.mapa[index_of_start+1:]
        before_start = self.mapa[:index_of_start]
        path = [start] + after_start + before_start + self.domceky[farba]
        return path

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


if __name__ == "__main__":    
    logika = Logika()
    pg.quit()