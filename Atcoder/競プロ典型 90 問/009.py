from math import atan2, degrees
from bisect import bisect_left

N = int(input())
points = [[int(i) for i in input().split()] for j in range(N)]
mag = 0
for i in range(N):
    angs = []
    for j in range(N):
        if i == j:
            continue
        X,Y = points[j][0] - points[i][0], points[j][1] - points[i][1]
        angs.append(degrees(atan2(Y, X)))
    angs.sort()
    for j in range(len(angs)):
        ind = bisect_left(angs, (angs[j] + 180) % 360)
        if ind != len(angs):
            mag = max(mag, min(abs(angs[j] - angs[ind]), 360-abs(angs[j] - angs[ind])))
        if ind > 0:
            mag = max(mag, min(abs(angs[j] - angs[ind-1]), 360-abs(angs[j] - angs[ind-1])))
print(mag)