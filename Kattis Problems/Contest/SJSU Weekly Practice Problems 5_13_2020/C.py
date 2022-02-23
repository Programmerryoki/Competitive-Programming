N,M = [int(i) for i in input().split()]
graph = {i:{} for i in range(1,N+1)}
A,B,K,G = [int(i) for i in input().split()]
g = [int(i) for i in input().split()]
for _ in range(M):
    a,b,l = [int(i) for i in input().split()]
    graph[a][b] = l
    graph[b][a] = l
print(graph)