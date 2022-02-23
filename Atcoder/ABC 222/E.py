N,M,K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
graph = {i:set() for i in range(1,N+1)}
for _ in range(N-1):
    U,V = [int(i) for i in input().split()]
    graph[U].add(V)
    graph[V].add(U)

