n,m,s,t = map(int, input().split())
graph = {i:set() for i in range(n)}
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)

squawk = [0]*n
squawk[s] = 1
for _ in range(t):
    # print(squawk)
    next = [0]*n
    for i in range(n):
        if squawk[i]:
            for nei in graph[i]:
                next[nei] += squawk[i]
    squawk = next
print(sum(squawk))