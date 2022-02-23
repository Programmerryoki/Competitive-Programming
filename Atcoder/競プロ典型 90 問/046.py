from collections import Counter

MOD = 46

N = int(input())
A = [int(i) % MOD for i in input().split()]
B = [int(i) % MOD for i in input().split()]
C = [int(i) % MOD for i in input().split()]
AC = Counter(A)
BC = Counter(B)
CC = Counter(C)
total = 0
for a in AC:
    for b in BC:
        for c in CC:
            if (a + b + c) % 46 == 0:
                total += AC[a] * BC[b] * CC[c]
print(total)