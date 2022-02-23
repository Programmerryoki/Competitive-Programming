from collections import deque

N = int(input())
graph = {i:set() for i in range(1,N+1)}
for _ in range(N-1):
    A,B = [int(i) for i in input().split()]
    graph[A].add(B)
    graph[B].add(A)

def distance(start):
    dist = [-float("inf")] * (N+1)
    dist[start] = 0
    que = deque([start])
    while que:
        node = que.popleft()
        for n in graph[node]:
            if dist[n] == -float("inf"):
                dist[n] = dist[node] + 1
                que.append(n)
    return dist

dist = distance(1)

ind = -1
m = -float("inf")
for i,d in enumerate(dist):
    if d > m:
        m = d
        ind = i

dist = distance(ind)

print(max(dist) + 1)