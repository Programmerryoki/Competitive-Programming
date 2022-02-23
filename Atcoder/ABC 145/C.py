from itertools import permutations
N = int(input())
pos = [[int(i) for i in input().split()] for j in range(N)]
total = 0
l = 0
for p in permutations([i for i in range(N)], N):
    l += 1
    for j in range(len(p)-1):
        x1,y1 = pos[p[j]]
        x2,y2 = pos[p[j+1]]
        total += ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(total / l)