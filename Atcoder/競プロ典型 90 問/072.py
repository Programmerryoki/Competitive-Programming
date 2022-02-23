H,W = [int(i) for i in input().split()]
C = [input() for i in range(H)]
moves = [(1,0),(-1,0),(0,1),(0,-1)]

def recur(start, cur, used):
    ml = 1
    for dx, dy in moves:
        x,y = dx+cur[0], dy+cur[1]
        if 0 <= x < H and 0 <= y < W and C[x][y] != "#":
            tup = (x,y)
            if tup in used and tup == start:
                ml = max(ml, len(used))
            if tup not in used:
                l = recur(start, tup, used | {tup})
                ml = max(ml, l)
    return ml

maxl = 0
for i in range(H):
    for j in range(W):
        if C[i][j] != ".":
            continue
        t = (i,j)
        dis = recur(t, t, {t})
        if dis > maxl:
            maxl = dis
print(maxl if maxl > 2 else -1)