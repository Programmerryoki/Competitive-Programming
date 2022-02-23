H,W = [int(i) for i in input().split()]
S = [list(input()) for i in range(H)]
box = [[1,0], [-1,0], [0,1], [0,-1]]
pos = True
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            for dx,dy in box:
                x,y = i+dx, j+dy
                if 0 <= x < H and 0 <= y < W and S[x][y] == "#":
                    break
            else:
                pos = False
print("Yes" if pos else "No")