from math import ceil
N = int(input())
A = [int(i) for i in input().split()]
A.sort(reverse=True)
c = 0
for i in range((N+1)//2):
    c += A[i]*2
print(c - A[0] - A[(N-1)//2]*((N)&1))