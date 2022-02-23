from sys import stdin
from collections import deque

input = stdin.readline
N = int(input())
graph = {i+1:set() for i in range(N)}
times = [0]*(N+1)
for I in range(N):
    T,K,*A = [int(i) for i in input().split()]
    times[I+1] = T
    for a in A:
        graph[I+1].add(a)

que = deque([N])
seen = {N}
td = times[N]
while que:
    cur = que.popleft()
    for nxt in graph[cur]:
        if nxt not in seen:
            seen.add(nxt)
            td += times[nxt]
            que.append(nxt)
print(td)