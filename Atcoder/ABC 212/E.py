MOD = 998244353

def multiply(A,B):
    # for i in A:
    #     print(i)
    # print()
    # for i in B:
    #     print(i)
    # print("-"*10)
    la = len(A); lb = len(B[0])
    c = len(B)
    ans = [[0]*lb for i in range(la)]
    for i in range(la):
        for j in range(lb):
            for k in range(c):
                ans[i][j] += A[i][k] * B[k][j]
            ans[i][j] %= MOD
    return ans

N,M,K = [int(i) for i in input().split()]
matrix = [[1]*N for i in range(N)]
for _ in range(M):
    U,V = [int(i)-1 for i in input().split()]
    matrix[U][V] = 0
    matrix[V][U] = 0
for i in range(N):
    matrix[i][i] = 0

num = bin(K)[2:][::-1]
mul2 = [matrix]
for i in range(len(num)):
    mul2.append(multiply(mul2[-1], mul2[-1]))

ans = [[0] for i in range(N)]
ans[0] = [1]
# for i in range(K):
#     ans = multiply(mul2[0], ans)
#     print(ans)
# print(ans[0])
for i,v in enumerate(num):
    if v == "1":
        ans = multiply(mul2[i], ans)
        # print(ans)
print(ans[0][0])