import heapq
from collections import deque

N,M = [int(i) for i in input().split()]
X,Y = [int(i) for i in input().split()]
posi = [[int(i) for i in input().split()] for j in range(N)]
graph = {i:{} for i in range(1,N+1)}
for _ in range(M):
    p,q = [int(i) for i in input().split()]
    d = ((posi[p-1][0] - posi[q-1][0])**2 + (posi[p-1][1] - posi[q-1][1])**2)**0.5
    graph[p] = [q,d]
    graph[q] = [p,d]

pos = [float("inf")]*N
que = deque([X])
seen = {X}
while que:
    node = que.popleft()
    for n in graph[node]:
        if n not in seen:
            seen.add(n)
            heapq.heappush(que)