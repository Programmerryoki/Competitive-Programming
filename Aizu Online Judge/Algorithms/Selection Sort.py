N = int(input())
A = [int(i) for i in input().split()]
c = 0
for i in range(0,N):
    minj = i
    for j in range(i, N):
        if A[j] < A[minj]:
            minj = j
    A[i], A[minj] = A[minj], A[i]
    if i != minj:
        c += 1
print(" ".join(map(str, A)))
print(c)