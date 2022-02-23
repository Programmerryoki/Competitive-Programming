MOD = 10**9 + 7

N,L = [int(i) for i in input().split()]
dp = [0]*(N+1)
dp[0] = 1
for i in range(len(dp)-1):
    dp[i+1] += dp[i]
    dp[i+1] %= MOD
    if i+L < len(dp):
        dp[i+L] += dp[i]
        dp[i+L] %= MOD
print(dp[N])