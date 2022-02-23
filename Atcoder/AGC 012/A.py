N = int(input())
A = [int(i) for i in input().split()]
A.sort()
A = A[N:]
t = 0
for i in range(0,2*N,2):
    t += A[i]
print(t)