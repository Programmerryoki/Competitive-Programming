from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
paths = []
graph = {i:set() for i in range(N+1)}
for i in range(N-1):
    a,b = [int(i)-1 for i in input().split()]
    paths.append((a,b))
    graph[a].add(b)
    graph[b].add(a)

dp = [0]*(N+1)
def dfs(pos, pre):
    global dp
    dp[pos] = 1
    for i in graph[pos]:
        if i != pre:
            dfs(i, pos)
            dp[pos] += dp[i]

dfs(0,-1)
ans = 0
for i in range(N-1):
    A,B = paths[i]
    r = min(dp[A], dp[B])
    ans += r * (N - r)
print(ans)