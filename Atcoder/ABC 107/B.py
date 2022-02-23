H,W = [int(i) for i in input().split()]
A = [list(input()) for i in range(H)]
i = 0
while i < len(A):
    if A[i].count(".") == len(A[0]):
        del A[i]
    else:
        i += 1
i = 0
while i < len(A[0]):
    if [j[i] for j in A].count(".") == len(A):
        for j in range(len(A)):
            del A[j][i]
    else:
        i += 1
print("\n".join("".join(i) for i in A))