# ALDS1_2_A

N = int(input())
A = [int(i) for i in input().split()]
c = 0
flag = 1
while flag:
    flag = 0
    for j in range(N-1, 0, -1):
        if A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            flag = 1
            c += 1
print(" ".join(map(str, A)))
print(c)