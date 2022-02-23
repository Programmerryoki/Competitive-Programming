from math import log2, ceil

N,K = [int(i) for i in input().split()]
MOD = 10**9 + 7
if N == 1:
    print(K % MOD)
    exit()
if N == 2:
    print((K * (K-1)) % MOD)
    exit()
if K < 3:
    print(0)
    exit()
ans = (K * (K-1)) % MOD
mulK = [K-2]
for i in range(ceil(log2(N))):
    mulK.append((mulK[-1])**2 % MOD)
# print(mulK)
n = bin(N-2)[2:][::-1]
# print(n)
for i in range(len(n)):
    if n[i] == "1":
        ans *= mulK[i]
        ans %= MOD
print(ans)