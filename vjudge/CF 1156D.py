from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
graph = {i:{} for i in range(1,n+1)}
types = [0]*n
for _ in range(n-1):
    x,y,c = [int(i) for i in input().split()]
    graph[x][y] = c
    graph[y][x] = c
    types[x-1] |= 1<<c
    types[y-1] |= 1<<c
# print([bin(i)[2:][::-1] for i in types])

total = 0
group = [[],[]]
connect = [[-1,-1] for i in range(n)]
seen = [set(), set()]
for i in range(1,n+1):
    for typ in range(2):
        if i in seen[typ] or not types[i-1] & (1<<typ):
            continue
        seen_i = {i}
        que = deque([i])
        while que:
            cur = que.popleft()
            for nxt in graph[cur]:
                if nxt not in seen_i and graph[cur][nxt] == typ:
                    que.append(nxt)
            seen_i.add(cur)
        seen[typ] |= seen_i
        for t in seen_i:
            connect[t-1][typ] = len(group[typ])
        group[typ].append(len(seen_i))
        total += (len(seen_i)*(len(seen_i)-1))
# print(group)
# print(connect)
for i in range(n):
    t0,t1 = connect[i]
    if t0>=0 and t1>=0:
        total += (group[0][t0]-1) * (group[1][t1]-1)
print(total)