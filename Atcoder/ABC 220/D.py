from collections import deque

MOD = 998244353

N = int(input())
A = [int(i) for i in input().split()]
dp = [0]*10
dp[A[0]] = 1
for i in range(1,N):
    new = [0]*10
    for j in range(10):
        new[(j + A[i])%10] += dp[j]
        new[(j * A[i])%10] += dp[j]
    for j in range(10):
        new[j] %= MOD
    dp = new
print("\n".join(map(str, dp)))