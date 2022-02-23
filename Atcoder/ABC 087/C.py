N = int(input())
A = [[int(i) for i in input().split()] for j in range(2)]
dp = [[0]*(N+1) for i in range(3)]
for i in range(1,3):
    for j in range(1,N+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + A[i-1][j-1]
print(dp[-1][-1])