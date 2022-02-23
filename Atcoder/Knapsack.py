N,W = [int(i) for i in input().split()]
items = [[int(i) for i in input().split()] for j in range(N)]
dp = [[-float("inf")]*(W+1) for i in range(N+1)]
dp[0][0] = 0
for i in range(N):
    w,v = items[i]
    for j in range(W):
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        if dp[i][j] == -float("inf"):
            continue
        if w + j > W:
            continue
        dp[i+1][j+w] = max(dp[i][j+w], dp[i][j] + v)
print(max(dp[-1]))