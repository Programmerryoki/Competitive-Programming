from collections import deque
n,m = [int(i) for i in input().split()]
grid = ["."*m for _ in range(n)]+[input() for i in range(n)]
moves = [(1,0),(-1,0),(0,1),(0,-1)]

def search(i,j):
    que = deque([(i,j)])
    seen = {(i,j)}
    letter = grid[i][j]
    while que:
        i,j = que.popleft()
        grid[i][j] = "."
        for dx,dy in moves:
            x,y = dx+i,dy+j
            if 0<=x<len(grid) and 0<=y<m and grid[x][y]==letter and (x,y) not in seen:
                seen.add((x,y))
                que.append((x,y))
    return seen

def dfs(used, ):
    for i in range(n,2*n):
        for j in range(m):
            if grid[i][j] == ".":
                continue
            letter = grid[i][j]
            search(i,j)

dfs(0,0)