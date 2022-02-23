H,W = [int(i) for i in input().split()]
line = [input() for i in range(H)]
ans = [[0]*W for i in range(H)]
dir = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
for i in range(H):
    for j in range(W):
        if line[i][j] == "#":
            for a,b in dir:
                x = i+a
                y = j+b
                if 0 <= x < H and 0 <= y < W:
                    if ans[x][y] != "#":
                        ans[x][y] += 1
            ans[i][j] = "#"
print("\n".join("".join(map(str, i)) for i in ans))