H,W = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for j in range(H)]
B = [[int(i) for i in input().split()] for j in range(H)]
count = 0
for i in range(H-1):
    for j in range(W-1):
        if A[i][j] != B[i][j]:
            dif = B[i][j] - A[i][j]
            count += abs(dif)
            A[i][j] += dif
            A[i+1][j] += dif
            A[i][j+1] += dif
            A[i+1][j+1] += dif
print(f"Yes\n{count}" if A == B else "No")