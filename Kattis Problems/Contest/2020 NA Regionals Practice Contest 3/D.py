from collections import deque

n,m = map(int, input().split())
graph = {i:{} for i in range(n)}
for i in range(m):
    a,b,d = map(int, input().split())
    graph[a][b] = d
    graph[b][a] = d

dist = [-1]*n
que = deque([1])
seen = {1}
while que:
    cur = que.popleft()
    for node in graph[cur]:
        if not node in seen:
            que.append(node)
            dist[node] = cur
            seen.add(node)
print(dist)