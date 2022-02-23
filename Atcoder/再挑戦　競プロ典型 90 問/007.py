from bisect import bisect_left

N = int(input())
A = [int(i) for i in input().split()]
A.sort()
Q = int(input())
for _ in range(Q):
    B = int(input())
    ind = bisect_left(A, B)
    mdif = float("inf")
    if ind < len(A):
        mdif = min(mdif, abs(B - A[ind]))
    if ind > 0:
        mdif = min(mdif, abs(B - A[ind-1]))
    print(mdif)