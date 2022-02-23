from bisect import bisect_left

N,M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
B.sort()
mind = float("inf")
for a in A:
    ind = bisect_left(B, a)
    if ind < len(B):
        d = abs(a - B[ind])
        if d < mind:
            mind = d
    if ind > 0:
        d = abs(a - B[ind-1])
        if d < mind:
            mind = d
print(mind)