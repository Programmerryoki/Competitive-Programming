H,W,C,Q = [int(i) for i in input().split()]
query = [[int(i) for i in input().split()] for _ in range(Q)]
usedrow = set()
usedcol = set()
color = [0]*C
for t,n,c in query[::-1]:
    if t == 1:
        if n in usedrow:
            continue
        color[c-1] += W - len(usedcol)
        usedrow.add(n)
    else:
        if n in usedcol:
            continue
        color[c-1] += H - len(usedrow)
        usedcol.add(n)
print(" ".join(map(str, color)))