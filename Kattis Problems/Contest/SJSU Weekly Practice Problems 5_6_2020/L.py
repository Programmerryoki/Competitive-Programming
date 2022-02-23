n,m,s,t = [int(i) for i in input().split()]
graph = {i:set() for i in range(0,n)}
for _ in range(m):
    x,y = [int(i) for i in input().split()]
    graph[x].add(y)
    graph[y].add(x)
sq = [0]*n
sq[s] = 1
for _ in range(t):
    t = [0]*n
    for i,nu in enumerate(sq):
        if nu:
            for j in graph[i]:
                t[j] += nu
    sq = t
print(sum(sq))