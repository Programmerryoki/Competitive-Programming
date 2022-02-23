N,D = [int(i) for i in input().split()]
walls = [[int(i) for i in input().split()] for _ in range(N)]
walls.sort(key=lambda x: (x[1], x[0]))
count = 0
pp = -1
for L,R in walls:
    if pp == -1:
        pp = R
        count += 1
    if pp + D - 1 < L:
        pp = R
        count += 1
print(count)