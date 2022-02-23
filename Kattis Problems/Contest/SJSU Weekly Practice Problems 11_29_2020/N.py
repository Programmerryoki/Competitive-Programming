MOD = 10**9 + 7

T = int(input())
que = [int(input()) for i in range(T)]
m = max(que)
dp = [[0,0] for _ in [0]*(m+1)]
dp[1] = [1,1]
for i in range(2,m+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
    dp[i][1] = (dp[i-1][0]) % MOD

print(*[sum(dp[i])%MOD for i in que], sep="\n")