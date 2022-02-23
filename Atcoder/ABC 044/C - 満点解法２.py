N, A = [int(i) for i in input().split()]
x = [int(i) - A for i in input().split()]
X = max(x + [A])
dp = [[0]*2*N*X for i in range(N)]
dp[0][N*X] = 1
