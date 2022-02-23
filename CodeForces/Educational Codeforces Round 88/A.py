from math import ceil

t = int(input())
for _ in range(t):
    n,m,k = [int(i) for i in input().split()]
    nc = n//k
    if m <= nc:
        print(m)
    else:
        print(nc - ceil((m - nc)/(k-1)))