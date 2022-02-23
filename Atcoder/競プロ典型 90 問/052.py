MOD = 10**9 + 7

N = int(input())
A = [sum([int(i) for i in input().split()]) % MOD for j in range(N)]
total = 1
for a in A:
    total *= a
    total %= MOD
print(total)