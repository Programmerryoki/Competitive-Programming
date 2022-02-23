from bisect import bisect_right

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
A.sort()
B.sort()
C.sort()
count = 0
indb = -1
indc = -1
for i in range(N):
    a = A[i]
    indb = bisect_right(B, a, indb+1)
    if indb >= N:
        break
    b = B[indb]
    indc = bisect_right(C, b, indc+1)
    if indc >= N:
        break
    count += 1
print(count)