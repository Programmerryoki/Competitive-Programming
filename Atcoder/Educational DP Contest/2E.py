N,W = [int(i) for i in input().split()]
val = [[int(i) for i in input().split()] for j in range(N)]
width = 10**3 * N
# minimum weight to achieve that value
dp = [[float("inf")]*(width + 1) for i in range(N+1)]
dp[0][0] = 0
for i in range(N):
    w,v = val[i]
    for j in range(width):
        if dp[i][j] == float("inf"):
            continue
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        dp[i+1][j+v] = min(dp[i][j]+w, dp[i][j+v])

maxval = 0
for i in range(width+1):
    if dp[-1][i] <= W:
        maxval = i
print(maxval)