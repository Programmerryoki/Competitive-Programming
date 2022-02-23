from collections import deque

N,Q = [int(i) for i in input().split()]
graph = {i:set() for i in range(N)}
for _ in range(N-1):
    a,b = [int(i)-1 for i in input().split()]
    graph[a].add(b)
    graph[b].add(a)

color = [0]*N
que = deque([0])
seen = {0}
while que:
    node = que.popleft()
    for n in graph[node]:
        if n not in seen:
            color[n] = 1 - color[node]
            que.append(n)
            seen.add(n)
# print(color)

ans = [""] * Q
for q in range(Q):
    c,d = [int(i)-1 for i in input().split()]
    ans[q] = "Town" if color[c] == color[d] else "Road"
print("\n".join(ans))