H,W = map(int, input().split())
A = [[int(i) for i in input().split()] for j in range(H)]
rows = [sum(i) for i in A]
cols = [sum([A[i][j] for i in range(H)]) for j in range(W)]
B = [[0]*W for i in range(H)]
for i in range(H):
    for j in range(W):
        B[i][j] = rows[i] + cols[j] - A[i][j]
print("\n".join(" ".join(map(str,i)) for i in B))