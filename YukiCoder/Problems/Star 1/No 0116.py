N = int(input())
A = [int(i) for i in input().split()]
c = 0
for i in range(N-2):
    if A[i+1] < A[i] < A[i+2] or A[i+2] < A[i] < A[i+1]:
        c += 1
    elif A[i] < A[i+2] < A[i+1] or A[i+1] < A[i+2] < A[i]:
        c += 1
print(c)