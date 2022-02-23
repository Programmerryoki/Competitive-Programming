MOD = 10**9 + 7
N,B,K = map(int, input().split())
c = [int(i) for i in input().split()]
# 3
from math import log, ceil
bit = [10%B]
for i in range(1,60):
    bit.append((bit[-1]**2) % B)
ans = [0]*B
for i in c:
    ans[i % B] += 1
num = bin(N)[2:][::-1]
dp = [[0]*B for i in range(len(num)+1)]
for i in c:
    dp[0][i % B] += 1
for i in range(len(num)):
    for j in range(B):
        for k in range(B):
            nex = (j * bit[i] + k) % B
            dp[i+1][nex] += dp[i][j] * dp[i][k]
            dp[i+1][nex] %= MOD
print(bit)
print(num)
print(ans)
for i in range(len(num)):
    if num[i] != "1":
        continue
    tmp = [0]*B
    for j in range(B):
        for k in range(B):
            nex = (j * bit[i] + k) % B
            tmp[nex] += ans[j] * ans[k]
            tmp[nex] %= MOD
    ans = tmp
    print(ans)
print(ans[0])

# small 2
# def mulMatrix(a,b):
#     la = len(a)
#     lb = len(b[0])
#     C = [[0]*lb for i in range(la)]
#     for i in range(la):
#         for j in range(lb):
#             for k in range(B):
#                 C[i][j] += a[i][k] * b[k][j]
#                 C[i][j] %= MOD
#     return C
#
# from math import log, ceil
# A = [[0]*B for i in range(B)]
# for i in range(B):
#     for j in c:
#         A[i][(10*i + j) % B] += 1
# bit = [A]
# for k in range(1,ceil(log(N, 2))):
#     bit.append(mulMatrix(bit[-1],bit[-1]))
# # for i in bit:
# #     for j in i:
# #         print(j)
# #     print()
# num = bin(N)[2:][::-1]
# ans = [0 for i in range(B)]
# ans[0] = 1
# for i in range(len(num)):
#     if num[i] == "0":
#         continue
#     tmp = [0] * B
#     for j in range(B):
#         tmp[j] += sum(bit[i][j][k] * ans[k] for k in range(B))
#         tmp[j] %= MOD
#     ans = tmp
#     # print(ans)
# print(ans[0])


# small 1
# dp = [[0]*B for i in range(N+1)]
# dp[0][0] = 1
# for i in range(1, N+1):
#     for j in range(B):
#         for C in c:
#             dp[i][(10*j+C) % B] = (dp[i][(10*j+C) % B] + dp[i-1][j]) % MOD
# for i in dp:
#     print(i)
# print(dp[-1][0])