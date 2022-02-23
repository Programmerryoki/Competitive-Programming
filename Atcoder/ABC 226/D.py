from math import gcd

N = int(input())
points = [[int(i) for i in input().split()] for _ in range(N)]
points.sort()
magic = set()
for i in range(N):
    xi,yi = points[i]
    for j in range(N):
        if i == j:
            continue
        xj,yj = points[j]
        dx,dy = xj - xi, yj - yi
        g = gcd(dx,dy)
        dx,dy = dx // g, dy // g
        if (dx,dy) not in magic:
            magic.add((dx,dy))
print(len(magic))