# P = int(input())
# for _ in range(P):
#     K,N,v = [int(i) for i in input().split()]

from itertools import permutations
from math import factorial
for i in range(1,10):
    pdc = [0]*i
    for lst in permutations([k+1 for k in range(i)]):
        c = 0
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                c += 1
        pdc[c] += 1
    print(i,pdc, sum(pdc))