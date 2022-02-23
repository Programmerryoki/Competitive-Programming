from sys import stdin
from collections import deque

input = stdin.readline
N,M = [int(i) for i in input().split()]
graph = {i+1:{} for i in range(N)}
edges = []
for I in range(M):
    U,V = [int(i) for i in input().split()]
    graph[U][I] = 0
    graph[V][I] = 1
    edges.append((U,V))

leaf = []
for i in range(1,N+1):
    if len(graph[i]) == 1:
        leaf.extend(graph[i])

while leaf:
    print(leaf)
    cur = leaf.pop()
    for edge in graph[cur]:
        del graph[edges[edge][1-graph[cur][edge]]][edge]
        if len(graph[edges[edge][1-graph[cur][edge]]]) == 1:
            leaf.append(edges[edge][1-graph[cur][edge]])
    graph[cur] = {}

print(graph)