from math import log2, ceil

N = num = int(input())
pf = 0
for i in range(2, ceil(num**0.5)+1):
    while N%i == 0:
        pf += 1
        N //= i
if N != 1:
    pf += 1
print(ceil(log2(pf)) if pf else 0)