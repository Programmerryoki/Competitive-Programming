from collections import deque

move = {hex(i)[-1].upper():"0"*(4 - len(bin(i)[2:]))+bin(i)[2:] for i in range(16)}
moves = [[-1,0],[0,1],[1,0],[0,-1]]
res = ["01234567", "012389AB" , "014589CD", "02468ACE"]
while True:
    H,W = map(int, input().split())
    if H == 0 and W == 0:
        break
    maze = [input() for i in range(H)]
    ex = []
    for i in range(H):
        for j in range(W):
            if i == 0 and maze[i][j] in "01234567":
                ex.append((i,j))
            elif i == H-1 and maze[i][j] in "014589CD":
                ex.append((i,j))
            elif j == 0 and maze[i][j] in "02468ACE":
                ex.append((i,j))
            elif j == W-1 and maze[i][j] in "012389AB":
                ex.append((i,j))
    # print(ex)
    path = [[float("inf")]*W for i in range(H)]
    path[ex[0][0]][ex[0][1]] = 0
    que = deque([ex[0]])
    seen = set()
    mulpath = False
    while que:
        i,j = que.popleft()
        for k,b in enumerate(move[maze[i][j]]):
            if b == "1":
                continue
            dx,dy = moves[k]
            x = i+dx; y = j+dy
            if 0 <= x < H and 0 <= y < W:
                if (x,y) not in seen:
                    que.append((x,y))
                    path[x][y] = path[i][j] + 1
                    seen.add((x,y))
                else:
                    if path[i][j] - path[x][y] != 1:
                        # print((i,j),(x,y),path[i][j] - path[x][y])
                        mulpath = True
        seen.add((i,j))

    # for i in path:
    #     print(i)

    if path[ex[-1][0]][ex[-1][1]] == float("inf"):
        print("NO SOLUTION")
    elif sum([float("inf") in i for i in path]):
        print("UNREACHABLE CELL")
    elif mulpath:
        print("MULTIPLE PATHS")
    else:
        print("MAZE OK")