from math import ceil

n, r ,k = [int(i) for i in input().split()]
ss = 0
if r >= k:
    if n > r:
        ss += ceil((n-r)/2)*2 + 2*r
    elif n == r:
        ss += 2*r
    else:
        ss += 2*r
else:
    if n <= k + (k-r):
        ss += 2*k
    else:
        ss += ceil((n-(2*k-r))/2)*2 + 2*k
print(ss)