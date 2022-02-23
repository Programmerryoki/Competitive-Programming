N = int(input())
h = [int(i) for i in input().split()]
dp = [float("inf")]*(N)
dp[0] = 0
for i in range(N):
    if i+1 < N:
        dp[i+1] = min(dp[i]+abs(h[i]-h[i+1]), dp[i+1])
    if i+2 < N:
        dp[i+2] = min(dp[i]+abs(h[i]-h[i+2]), dp[i+2])
print(dp[-1])