H,W = [int(i) for i in input().split()]
C = [list(input()) for _ in range(H)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
for i in range(H):
    for j in range(W):
        if C[i][j] != ".":
            continue
        used = set()
        for dx,dy in move:
            if 0<=i+dx<H and 0<=j+dy<W:
                used.add(C[i+dx][j+dy])
        for c in range(1,6):
            if str(c) not in used:
                C[i][j] = str(c)
                break
print("\n".join("".join(i) for i in C))