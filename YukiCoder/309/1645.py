MOD = 998244353

N = int(input())
A = [int(i) for i in input().split()]
r = 100*N
w = r*2
dp = [[0]*(w+1) for i in range(N+1)]
dp[0][r] = 1
for i in range(N):
    num = A[i]
    for j in range(w+1):
        if dp[i][j] == 0:
            continue
        dp[i+1][j+num] += dp[i][j]
        dp[i+1][j-num] += dp[i][j]
total = 0
for i in range(w+1):
    total += abs(dp[-1][i] * (i-r))
    total %= MOD
print(total)