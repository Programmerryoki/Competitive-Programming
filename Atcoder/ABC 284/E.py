from sys import setrecursionlimit
setrecursionlimit(10**6)


N,M = [int(i) for i in input().split()]
graph = {i:[] for i in range(N)}
for _ in range(M):
    u,v = [int(i)-1 for i in input().split()]
    graph[u].append(v)
    graph[v].append(u)

def dfs(cur, prev, seen):
