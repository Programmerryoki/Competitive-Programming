from math import atan2, degrees
from bisect import bisect_left

def angle(x,y):
    return 180 + degrees(atan2(x,y))

N = int(input())
points = [[int(i) for i in input().split()] for j in range(N)]
maxang = 0
for i,j in points:
    angs = []
    for x,y in points:
        if i == x and j == y:
            continue
        angs.append(angle(x - i,y - j))
    angs.sort()
    for ang in angs:
        ind = bisect_left(angs, (ang + 180) % 360)
        if ind < len(angs):
            d = (ang - angs[ind] + 360) % 360
            if abs(d - 180) < abs(maxang - 180):
                maxang = min(d, 360 - d)
        if ind > 0:
            d = (ang - angs[ind-1] + 360) % 360
            if abs(d - 180) < abs(maxang - 180):
                maxang = min(d, 360 - d)
print(maxang)