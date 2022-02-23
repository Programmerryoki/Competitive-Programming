N = int(input())
A = [int(i) for i in input().split()]

c = 0
for i in range(N-1):
    s = A[i]
    for j in range(i+A[i],N):
