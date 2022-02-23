K = int(input())
S = input()
MOD = 10**9 + 7
t = 0
for i in range(K+1):
    t += (25**i * 26**(K-i))%MOD
print(t%MOD)