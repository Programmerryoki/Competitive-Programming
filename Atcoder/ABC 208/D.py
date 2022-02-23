import heapq

N,M = [int(i) for i in input().split()]
graph = {i:{} for i in range(N)}
for _ in range(M):
    A,B,C = [int(i) for i in input().split()]
    graph[A-1][B-1] = C

total = 0
