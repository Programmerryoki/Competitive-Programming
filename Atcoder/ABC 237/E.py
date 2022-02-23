from sys import stdin
from collections import deque

input = stdin.readline
N,M = [int(i) for i in input().split()]
H = [int(i) for i in input().split()]
graph = {i:set() for i in range(N)}
for _ in range(M):
    U,V = [int(i)-1 for i in input().split()]
    graph[U].add(V)
    graph[V].add(U)

md = [-float("inf") for i in range(N)]
md[0] = 0
que = deque([[0, 0]])
while que:
    d, cur = que.popleft()
    if d < md[cur]:
        continue
    for nxt in graph[cur]:
        if H[cur] > H[nxt] and md[nxt] < md[cur] + (H[cur]-H[nxt]):
            md[nxt] = md[cur] + (H[cur]-H[nxt])
            que.append([md[nxt], nxt])
        elif H[cur] < H[nxt] and md[nxt] < md[cur] - 2 * (H[nxt]-H[cur]):
            md[nxt] = md[cur] - 2 * (H[nxt]-H[cur])
            que.append([md[nxt], nxt])
        elif H[cur] == H[nxt] and md[nxt] < md[cur]:
            md[nxt] = md[cur]
            que.append([md[nxt],nxt])
print(max(md))