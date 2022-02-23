n = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
j = B.index(A[0])
c = 0
nx = -1
for i in range(n):
    if A[i] == B[(i+j)%n]:
        c += 1
    else:
        nx = i
j = B.index(A[nx])
c2 = 0
for i in range(n):
    if A[(nx + i)%n] == B[(i+j+nx)%n]:
        c2 += 1
print(max(c,c2))