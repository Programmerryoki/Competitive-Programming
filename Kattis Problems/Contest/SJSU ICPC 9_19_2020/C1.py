from collections import deque
from sys import stdin

input = stdin.readline

N,H,L = map(int, input().split())
X = [int(i) for i in input().split()]
movies = [float("inf")]*N
for i in X:
    movies[i] = 0

graph = {i:set() for i in range(N)}
for _ in range(L):
    a,b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

for id in X:
    que = deque([id])
    seen = {id}
    while que:
        i = que.popleft()
        for c in graph[i]:
            if c not in seen:
                movies[c] = min(movies[c], movies[i] + 1)
                seen.add(c)
                que.append(c)
print(movies.index(max(movies)))