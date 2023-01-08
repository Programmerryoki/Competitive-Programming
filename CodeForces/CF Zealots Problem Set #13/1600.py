t = int(input())
for _ in range(t):
    input()
    n,k = [int(i) for i in input().split()]
    graph = {i:[] for i in range(n)}
    for _ in range(n-1):
        u,v = [int(i)-1 for i in input().split()]
        graph[u].append(v)
        graph[v].append(u)
    dis = [float("inf") if len(graph[i]) > 1 else 1 for i in range(n)]
    def dfs(cur, prev):
        md = float("inf")
        for nxt in graph[cur]:
            if nxt == prev:
                continue
            dfs(nxt, cur)
            md = min(md, dis[nxt]+1)
        dis[cur] = min(md, dis[cur])

    dfs(0, -1)
    print(sum(i > k for i in dis))