dp = [[0]*10 for i in range(10)]
for i in range(10):
    for j in range(10):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + dp[i][j-1])
for i in dp:
    print(i)