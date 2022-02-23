N = int(input())
W = [int(i) for i in input().split()]
sw = sum(W)
dp = [[0]*(sw+1) for i in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for j in range(0,sw+1):
        if j - W[i-1] >= 0:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-W[i-1]]
        else:
            dp[i][j] = dp[i-1][j]
print("impossible"[2*(dp[-1][sw//2] and (sw/2).is_integer()):])