from collections import deque

N,M = map(int, input().split())
graph = {i:set() for i in range(N)}
for _ in range(M):
    A,B = [int(i)-1 for i in input().split()]
    graph[A].add(B)

total = 0
for i in range(N):
    que = deque([i])
    seen = {i}
    while que:
        node = que.popleft()
        for n in graph[node]:
            if n not in seen:
                que.append(n)
                seen.add(n)
    total += len(seen)
print(total)