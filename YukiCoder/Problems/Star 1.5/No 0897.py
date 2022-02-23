from math import ceil, log
Q = int(input())
for _ in range(Q):
    n,k = [int(i) for i in input().split()]
    if k > 1:
        print(ceil(log(n, k)))
    else:
        print(n - 1)