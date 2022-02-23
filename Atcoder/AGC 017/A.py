from math import comb
from collections import Counter

N,P = [int(i) for i in input().split()]
A = [int(i)&1 for i in input().split()]
total = 0
CS = Counter(A)
odd = []
for i in range(CS[1]+1):
    odd.append(comb(CS[1], i))
even = 2**CS[0]
total = 0
for i in range(len(odd)):
    if i&1 != P:
        continue
    total += odd[i] * even
print(total)