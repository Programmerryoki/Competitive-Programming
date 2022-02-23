MOD = 998244353

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
dp = [0]*(3001)
dp[0] = 1
for i in range(N):
    cs = 0
    for j in range(B[i]+1):
        cs += dp[j]
        cs %= MOD
        if j < A[i]:
            dp[j] = 0
        else:
            dp[j] = cs
print((sum(dp[A[-1]:B[-1]+1]))%MOD)

# MOD = 998244353
#
# N = int(input())
# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]
# dpb = [0]*(3001)
# dpb[0] = 1
# csa = 1
# for i in range(N):
#     csb = 0; csa *= A[i]; csa %= MOD
#     for j in range(B[i]+1):
#         csb += dpb[j]
#         csb %= MOD
#         dpb[j] = csb
#     print(B[i], dpb)
#     print(csa)
# print((sum(dpb)-csa-1)%MOD)