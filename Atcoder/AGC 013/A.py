N = int(input())
A = [int(i) for i in input().split()]
nb = 0
da = 0
for i in range(len(A)-1):
    if A[i] > A[i+1] and da > 0:
        nb += 1
        da = 0
    elif A[i] < A[i+1] and da < 0:
        nb += 1
        da = 0
    else:
        if A[i+1] - A[i] != 0:
            da = A[i+1] - A[i]
print(nb + 1)