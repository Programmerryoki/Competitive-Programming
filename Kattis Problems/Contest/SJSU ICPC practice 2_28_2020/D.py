n,m,q = [int(i) for i in input().split()]
nodes = [[-9999]*n for i in range(n)]

def bfs(start, end):
    ans = [start]
    que = []
    while True:
        n = ans[-1]
        que = [i for i in range(n) if nodes[n][i] != -9999]


for a in range(m):
    u,v,w = [int(i) for i in input().split()]
    nodes[u][v] = w
    nodes[v][u] = w
