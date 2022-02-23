H,W = [int(i) for i in input().split()]
grid = [input() for i in range(H)]
dp = [[0]*(W+1) for i in range(H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        if grid[i-1][j-1] == ".":
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        if i == j == 1:
            dp[i][j] = 1
print(dp[-1][-1]%(10**9+7))