n = int(input())
p = [-1]*2+[int(i) for i in input().split()]
graph = {i:set() for i in range(-1,n+1)}
for i,N in enumerate(p):
    graph[N].add(i)
print(graph)

