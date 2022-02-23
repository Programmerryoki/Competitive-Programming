from collections import deque

N = int(input())
graph = {i:set() for i in range(N)}
for _ in range(N-1):
    A,B = [int(i)-1 for i in input().split()]
    graph[A].add(B)
    graph[B].add(A)

que = deque([0])
seen = {0}
dis = [float("inf")]*N
dis[0] = 0
while que:
    node = que.popleft()
    for n in graph[node]:
        if n not in seen:
            seen.add(n)
            que.append(n)
            dis[n] = min(dis[n], dis[node]+1)
# print(dis)
m = dis.index(max(dis))
que.clear()
que.append(m)
seen.clear()
seen.add(m)
dis = [float("inf")]*N
dis[m] = 0
while que:
    node = que.popleft()
    for n in graph[node]:
        if n not in seen:
            seen.add(n)
            que.append(n)
            dis[n] = min(dis[n], dis[node]+1)
print(max(dis)+1)