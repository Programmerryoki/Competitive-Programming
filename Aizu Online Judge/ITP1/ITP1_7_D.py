n, m, l = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(n)]
b = [[int(i) for i in input().split()] for j in range(m)]
ans = [[0]*l for i in range(n)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            ans[i][j] += a[i][k]*b[k][j]
print("\n".join(" ".join(map(str, i)) for i in ans))