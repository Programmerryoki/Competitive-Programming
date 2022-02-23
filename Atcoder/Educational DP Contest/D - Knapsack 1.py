N,W = [int(i) for i in input().split()]
wv = [[int(i) for i in input().split()] for j in range(N)]
dp = [[0]*(W+1) for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1, W+1):
        if 0 <= j-wv[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wv[i-1][0]] + wv[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])