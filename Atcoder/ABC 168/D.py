from collections import deque

N,M = [int(i) for i in input().split()]
graph = {i:set() for i in range(1,N+1)}
for _ in range(M):
    a,b = [int(i) for i in input().split()]
    graph[a].add(b)
    graph[b].add(a)

path = {1:0}
seen = set([1])
que = deque([1])
while que:
    node = que.popleft()
    for n in graph[node]:
        if n not in seen:
            seen.add(n)
            que.append(n)
            path[n] = node

if len(seen) != N:
    print("No")
else:
    print("Yes")
    for i in range(2,N+1):
        print(path[i])