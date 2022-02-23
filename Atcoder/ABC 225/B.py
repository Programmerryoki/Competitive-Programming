N = int(input())
graph = {i+1:set() for i in range(N)}
for _ in range(N-1):
    a,b = [int(i) for i in input().split()]
    graph[a].add(b)
    graph[b].add(a)

count = 0
for key in graph:
    if len(graph[key]) == 1:
        count += 1
print("Yes" if count == N-1 else "No")