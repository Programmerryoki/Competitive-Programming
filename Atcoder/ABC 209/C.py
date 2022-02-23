N = int(input())
C = [int(i) for i in input().split()]
C.sort()
total = 1
MOD = 10**9 + 7
for i,c in enumerate(C):
    total *= c - i
    total %= MOD
print(total if total >= 0 else 0)