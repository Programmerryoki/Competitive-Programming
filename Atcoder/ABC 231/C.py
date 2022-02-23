from bisect import bisect_left

N,Q = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A.sort()
for _ in range(Q):
    x = int(input())
    print(N - bisect_left(A, x))