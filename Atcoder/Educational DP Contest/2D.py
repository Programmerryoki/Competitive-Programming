N,W = [int(i) for i in input().split()]
val = [[int(i) for i in input().split()] for j in range(N)]
dp = [[-float("inf")]*(W+1) for i in range(N+1)]
dp[0][0] = 0
for i in range(N):
    w,v = val[i]
    for j in range(W):
        if dp[i][j] == -float("inf"):
            continue
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        if j+w <= W:
            dp[i+1][j+w] = max(dp[i][j] + v, dp[i][j+w])
print(max(dp[-1]))