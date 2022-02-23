M,N = [int(i) for i in input().split()]
valut = [[int(i) for i in input().split()] for j in range(M)]
dp = [[float("inf") for i in range(N+1)] for j in range(M+1)]
dp[-1][-1] = 0
for i in range(M, 0, -1):
    for j in range(N, 0, -1):
        dp[i][j] = 