from heapq import heappush, heappop

N,M = [int(i) for i in input().split()]
graph = {i+1:[] for i in range(N)}
for _ in range(M):
    A,B,C = [int(i) for i in input().split()]
    graph[A].append((C,B))
    if A != B:
        graph[B].append((C,A))

edges = []
seen = set()
for i in graph[1]:
    heappush(edges, (i,1))
    seen.add((i[1],0,i[0]))
    seen.add((0,i[1],i[0]))
visited = {1}
adding = 0
while len(visited) < N:
    (cost, cur), prev = heappop(edges)
    if cur in visited:
        continue
    seen.add((cur,prev,cost))
    seen.add((prev,cur,cost))
    visited.add(cur)
    for nxt in graph[cur]:
        if nxt[1] not in visited:
            heappush(edges, (nxt, cur))
s = 0
for i in graph:
    for j in graph[i]:
        if (i,j[1],j[0]) not in seen:
            seen.add((i,j[1],j[0]))
            seen.add((j[1],i,j[0]))
            s += max(0, j[0])
print(s + adding)