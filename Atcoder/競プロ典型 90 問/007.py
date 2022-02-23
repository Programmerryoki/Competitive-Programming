from bisect import bisect_left

N = int(input())
A = [int(i) for i in input().split()]
A.sort()
Q = int(input())
for _ in range(Q):
    B = int(input())
    index = bisect_left(A, B)
    index -= index >= len(A)
    if index == 0:
        print(abs(A[index] - B))
    else:
        print(min(abs(A[index]-B), abs(A[index-1]-B)))