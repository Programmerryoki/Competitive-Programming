from collections import deque

N,M = [int(i) for i in input().split()]
graph = {i+1:set() for i in range(N)}
for i in range(M):
    a,b = [int(i) for i in input().split()]
    graph[a].add(b)
    graph[b].add(a)

que = deque([0])