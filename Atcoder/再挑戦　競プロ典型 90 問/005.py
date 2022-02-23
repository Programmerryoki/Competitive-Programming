N,B,K = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
MOD = 10**9 + 7

# 3
num = bin(N)[2:][::-1]
mul10 = [10%B]
for _ in range(len(num)):
    mul10.append((mul10[-1]**2) % B)
dp = [[0]*B for i in range(len(num)+1)]
for c in C:
    dp[0][c % B] += 1
for i in range(len(num)):
    for j in range(B):
        for k in range(B):
            nex = (j * mul10[i] + k) % B
            dp[i+1][nex] += dp[i][j] * dp[i][k]
            dp[i+1][nex] %= MOD
# print(dp)
ans = [0]*B
ans[0] += 1
for i in range(len(num)):
    if num[i] == "0":
        continue
    new = [0]*B
    for j in range(B):
        for k in range(B):
            nex = (j * mul10[i] + k) % B
            new[nex] += ans[j] * dp[i][k]
            new[nex] %= MOD
    ans = new
print(ans[0])


# 2
# def multiply(a,b):
#     tbl = type(b[0]) == list
#     la = len(a); lb = len(b[0]) if tbl else 1; lk = len(b)
#     tmp = [[0]*lb for i in range(la)]
#     for i in range(la):
#         for j in range(lb):
#             for k in range(lk):
#                 tmp[i][j] += a[i][k] * (b[k][j] if tbl else b[k])
#                 tmp[i][j] %= MOD
#     return tmp
#
# gyou = [[0]*B for i in range(B)]
# for i in range(B):
#     for c in C:
#         gyou[i][(i*10 + c) % B] += 1
# gyou_mul = [gyou]
# num = bin(N)[2:][::-1]
# for _ in range(len(num)):
#     gyou_mul.append(multiply(gyou_mul[-1], gyou_mul[-1]))
# ans = [0]*B
# ans[0] = 1
# for i in range(len(num)):
#     if num[i] == "1":
#         ans = multiply(gyou_mul[i], ans)
# print(ans[0][0])


# 1
# dp = [[0]*(B) for i in range(N+1)]
# dp[0][0] = 1
# for i in range(N):
#     for j in range(B):
#         if dp[i][j] == 0:
#             continue
#         for c in C:
#             dp[i+1][(j*10 + c) % B] += dp[i][j]
#             dp[i+1][(j*10 + c) % B] %= MOD
# print(dp[-1][0])