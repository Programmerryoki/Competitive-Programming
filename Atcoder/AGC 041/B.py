import sys
N,M,V,P = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
m = max(A)
c = 0
for a in A:
    if a+M >= m:
        c += 1
print(min(c,P))