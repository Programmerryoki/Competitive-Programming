from sys import setrecursionlimit, stdin
setrecursionlimit(10**6)
input = stdin.readline

N,Q = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]
graph = {i:set() for i in range(1, N+1)}
for _ in range(N-1):
    A,B = [int(i) for i in input().split()]
    graph[A].add(B)
    graph[B].add(A)
sl = {}

def dfs(cur, prev):
    bt = [X[cur-1]]
    for nxt in graph[cur]:
        if nxt != prev:
            bt += dfs(nxt, cur)
    bt.sort(reverse=True)
    bt = bt[:20]
    sl[cur] = bt
    return bt

dfs(1, -1)
ans = [0]*Q
for i in range(Q):
    v,k = [int(i) for i in input().split()]
    ans[i] = sl[v][k-1]
print("\n".join(str(i) for i in ans))