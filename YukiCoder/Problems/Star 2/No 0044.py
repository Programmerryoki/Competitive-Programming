N = int(input())
dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1
for i in range(2,len(dp)):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[-1])