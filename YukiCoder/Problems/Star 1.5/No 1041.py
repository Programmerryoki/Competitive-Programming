from decimal import Decimal

N = int(input())
coord = [[int(i) for i in input().split()] for j in range(N)]
m = 2
grad = lambda a,b: Decimal(b[1] - a[1]) / Decimal(b[0] - a[0]) if b[0] - a[0] != 0 else float("inf")
for i in range(N-1):
    for j in range(i+1,N):
        g = grad(coord[i], coord[j])
        c = 0
        for k in range(j+1, N):
            if grad(coord[j], coord[k]) == g:
                c += 1
        m = max(m, 2 + c)
print(m)