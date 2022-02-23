from collections import Counter
from math import ceil

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    half = len(a)/2
    cf = Counter(a[:ceil(half)])
    cb = Counter(a[int(half):])
    if cf == cb:
        print()
    print(cf)
    print(cb)
    print(cf == cb)
    cf.update(cb)
    print(cf)
    print()