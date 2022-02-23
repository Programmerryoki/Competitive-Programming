H,W = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for j in range(H)]
rows = [0]*H
cols = [0]*W
for i in range(H):
    for j in range(W):
        rows[i] += A[i][j]
        cols[j] += A[i][j]
for i in range(H):
    for j in range(W):
        A[i][j] = (rows[i] + cols[j]) - A[i][j]
print("\n".join(" ".join(map(str, i)) for i in A))