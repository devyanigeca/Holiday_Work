from collections import OrderedDict
from operator import itemgetter

def answer_do(list_do):
    a =  OrderedDict(sorted(enumerate(list_do), key=itemgetter(1))).keys()
    a = [x+1 for x in a]
    return a



def manhattan_distance(p1, p2):
    return abs(int(p1[0]) - int(p2[0])) + abs(int(p1[1]) - int(p2[1]))

islands = int(input().strip())

islands_raw = []

for _ in range(islands):
    islands_raw.append(input().strip())

ship = input().strip().split()
ship = (ship[0], ship[1])

island_dustances = []

for island in islands_raw:
    x1 = island.split()[0]
    y1 = island.split()[1]
    x2 = island.split()[2]
    y2 = island.split()[3]

    one_corner = (x1, y1)
    another_corner = (x2, y2)
    three_corner = (
        min(x1, x2), min(y1, y2) + abs(y1-y2)

    )
    four_corner = (
        min(x1, x2) + abs(x1 - x2) , min(y1, y2)
    )

    island_dustances.append(min(manhattan_distance(ship, one_corner), manhattan_distance(ship, another_corner)
                                , manhattan_distance(ship, three_corner), manhattan_distance(ship, four_corner)
                                ))

print(*answer_do(island_dustances), end='')