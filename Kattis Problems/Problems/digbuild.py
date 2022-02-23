from math import log2, ceil

MOD = 10**9 + 7

n = int(input())
if n == 1:
    print(5, )
    exit()
l2 = ceil(log2(n)) + 1
m2 = [0]*(l2)
m2[0] = 2
for i in range(1,l2):
    m2[i] = m2[i-1]**2 % MOD
print(m2)
ans = 1
i = 0
while n > 0:
    if n & 1:
        ans *= m2[i]
        ans %= MOD
    n >>= 1
    i += 1
print(ans)
print(ans * 3 + 1)


# dp = [[0]*3 for i in range(n+1)]
# dp[0] = [1,1,1]
# for i in range(1,n+1):
#     dp[i][0] = dp[i-1][1] + dp[i-1][2]
#     dp[i][1] = dp[i-1][0] + dp[i-1][2]
#     dp[i][2] = dp[i-1][0] + dp[i-1][1]
# for i in dp:
#     print(i)