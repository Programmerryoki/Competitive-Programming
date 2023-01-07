from collections import deque

N,M = [int(i) for i in input().split()]
graph = {i:[] for i in range(N)}
for _ in range(M):
    u,v = [int(i)-1 for i in input().split()]
    graph[u].append(v)
    graph[v].append(u)

seen = set()
tn = 0
for i in range(N):
    if i in seen:
        continue
    que = deque([i])
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if nxt not in seen:
                seen.add(nxt)
                que.append(nxt)
    tn += 1
print(tn)