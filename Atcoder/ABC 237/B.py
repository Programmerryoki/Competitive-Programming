H,W = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for _ in range(H)]
B = [[A[j][i] for j in range(H)] for i in range(W)]
print("\n".join(" ".join(str(i) for i in j) for j in B))