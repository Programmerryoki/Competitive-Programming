MOD = 10**9 + 7

N = int(input())
C = [""]+input().split()
graph = {i:set() for i in range(1,N+1)}
for _ in range(N-1):
    a,b = [int(i) for i in input().split()]
    graph[a].add(b)
    graph[b].add(a)

dp = [[0]*3 for i in range(N+1)]
def dfs(cur, pre):
    val1 = val2 = 1
    for i in graph[cur]:
        if i == pre:
            continue
        dfs(i, cur)
        if C[cur] == "a":
            val1 *= (dp[i][0] + dp[i][2])
            val2 *= (dp[i][0] + dp[i][1] + 2 * dp[i][2])
        if C[cur] == "b":
            val1 *= (dp[i][1] + dp[i][2])
            val2 *= (dp[i][0] + dp[i][1] + 2 * dp[i][2])
        val1 %= MOD
        val2 %= MOD
    if C[cur] == "a":
        dp[cur][0] = val1
        dp[cur][2] = (val2 - val1 + MOD) % MOD
    if C[cur] == "b":
        dp[cur][1] = val1
        dp[cur][2] = (val2 - val1 + MOD) % MOD
dfs(1, -1)
print(dp[1][2])