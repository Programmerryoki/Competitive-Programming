MOD = 998244353

N,D = [int(i) for i in input().split()]
numN = bin(N)[2:][::-1]
mul2 = [2]
for i in range(len(numN)):
    mul2.append((mul2[-1]**2)%MOD)
print(mul2)
total = 0
for i in range(-(-D//2), N):
for i in range(N, 2*N - D + 1):
