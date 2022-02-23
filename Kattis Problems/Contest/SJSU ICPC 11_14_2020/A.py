from collections import deque

while True:
    r,c = map(int, input().split())
    if r == 0 and c == 0:
        break
    grid = [list(input()) for i in range(r)]
    su = set()
    for j in range(c):
        if grid[-1][j] != " ":
            su.add((r-1,j))

    move = [[0,1],[0,-1],[1,0],[-1,0]]
    def bfs(grid, su):
        new = set()
        for s in su:
            que = deque([s])
            while que:
                i,j = que.popleft()
                for dx,dy in move:
                    x = i+dx; y = j+dy
                    if 0 <= x < r and 0 <= y < c and grid[x][y] != " ":
                        tup = (x,y)
                        if tup in su or tup in new:
                            continue
                        new.add(tup)
                        que.append(tup)
        su.update(new)

    # print(su,grid)
    while True:
        for j in range(c):
            if grid[-1][j] != " ":
                su.add((r-1, j))
        # print(grid[-1])
        # print(su)
        prev = [[i for i in j] for j in grid]
        bfs(grid, su)
        for i in range(r-2, -1, -1):
            for j in range(c-1, -1, -1):
                if grid[i][j] == " ":
                    continue
                tup = (i,j)
                if tup in su:
                    continue
                if grid[i+1][j] == " ":
                    grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
        # for i in grid:
        #     print(i)
        # print()
        if prev == grid:
            break
    print("\n".join("".join(i) for i in grid))
    print()