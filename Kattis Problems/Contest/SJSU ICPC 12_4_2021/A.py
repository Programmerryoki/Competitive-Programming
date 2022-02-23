N, D = [int(i) for i in input().split()]
graph = {"E":{}}
p = []
for _ in range(N):
    x,y,n,m = [int(i) for i in input().split()]
    t = (x,y)
    if t not in graph:
        graph[t] = {}
    if n:
        graph[t]["E"] = [0, n, t, "E"]
        graph["E"][t] = graph[t]["E"]
    for i,j in p:
        if ((x-i)**2+(y-j)**2)**0.5 <= t:
            graph[t][(i,j)] = [0, m, ]