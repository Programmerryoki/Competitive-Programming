from bisect import bisect_left
N,M,X = map(int, input().split())
A = [int(i) for i in input().split()]
print(min(bisect_left(A, X), len(A) - bisect_left(A, X)))