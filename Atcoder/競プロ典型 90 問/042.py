K = int(input())
if K % 9 != 0:
    print(0)
    exit()

dp = [0] * (K+1)
MOD = 10**9 + 7
dp[0] = 1
for i in range(1, K+1):
    B = min(i, 9)+1
    for j in range(1, B):
        dp[i] += dp[i-j]
        dp[i] %= MOD
# print(dp)
print(dp[K])