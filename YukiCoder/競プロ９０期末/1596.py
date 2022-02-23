N,M = [int(i) for i in input().split()]

mod = 10**9 + 7

def power(x, a):
    if a == 0:
        return 1
    elif a == 1:
        return x
    elif a % 2 == 0:
        return power(x, a//2) **2 % mod
    else:
        return power(x, a//2) **2 * x % mod

def modinv(x):
    return power(x, mod-2)

def binomial_coefficients(n, k):
    numera = 1  # 分子
    denomi = 1  # 分母

    for i in range(k):
        numera *= n-i
        numera %= mod
        denomi *= i+1
        denomi %= mod
    return (numera * modinv(denomi)) % mod

from math import comb

# S = comb(2*N, N) * 2 * N
S = binomial_coefficients(2*N, N) * 2 * N
# print(S)
for _ in range(M):
    t,x,y = [int(i) for i in input().split()]
    # S -= comb(2*N - (x+y+1), min(N-(x+1), N-(y+1)))
    if t == 1:
        S -= binomial_coefficients(2*N - (x+y+1), min(N-(x+1), N-(y+1)))
    #     S -= comb(2*N - (x+y+1), N-(x+1))
    #     print(2*N - (x+y+1), min(N-(x+1), N-(y+1)))
    elif t == 2:
        S -= binomial_coefficients(2*N - (x+y+1), N-(y+1))
    #     S -= comb(2*N - (x+y+1), N-(y+1))
    #     print(2*N - (x+y+1), N-(y+1))
    # print(2*N - (x+y+1), N-y+1, N-x+1, t)
    # S %= mod
    # print(S)
print(S % mod)