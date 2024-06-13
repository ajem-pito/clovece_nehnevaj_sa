mapa: list[tuple[int,int, str]] = [
        (1, 5, None), (3, 5, None), (5, 5, None), (7, 5, None), (7, 4, None), (7, 3, None), (7, 2, None), (7, 1, None), 
        (9, 1, None), (11, 1, None), (13, 1, None), (13, 2, None), (13, 3, None), (13, 4, None), (13, 5, None), (15, 5, None),
        (17, 5, None), (19, 5, None), (19, 6, None), (19, 7, None), (19, 8, None), (19, 9, None), (17, 9, None), (15, 9, None),
        (13, 9, None), (13, 10, None), (13, 11, None), (13, 12, None), (13, 13, None), (11, 13, None), (9, 13, None), (7, 13, None),
        (7, 12, None), (7, 13, None), (7, 12, None), (7, 11, None), (7, 10, None), (7, 9, None), (5, 9, None), (3, 9, None), (1, 9, None),
        (1, 8, None), (1, 7, None), (1, 6, None)
    ]
        
domceky = {
        "red":[(3,7, None), (4, 7, None), (5, 7, None), (6, 7, None)],
        "blue":[(10,8, None), (10,9, None), (10,10, None), (10,11, None)],
        "green":[(10,3, None), (10,4, None), (10,5, None), (10,6, None)],
        "yellow":[(14, 7, None), (15, 7, None), (16, 7, None), (17, 7, None)]
        }

start = (9,1, None)
color = "green"

# loop which will make a path for the player to follow, if I start on (9,1) and I want to get to (1,5) I would need to go thru all the points in the list

index_of_start = mapa.index(start)

after_start = mapa[index_of_start+1:]
before_start = mapa[:index_of_start]

# print(after_start)
# print(before_start)

path = after_start + before_start + domceky[color]

print(path)


def vytvor_cestu(panacik, start):
    index_of_start = mapa.index(start)
    after_start = mapa[index_of_start+1:]
    before_start = mapa[:index_of_start]
    path = after_start + before_start + domceky[color]
    return path