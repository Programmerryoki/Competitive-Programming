from collections import deque

moves = [(0,1),(1,0)]

H,W = [int(i) for i in input().split()]
grid = [input() for i in range(H)]
que = deque([(0,0)])
lp = [[0]*W for _ in range(H)]
lp[0][0] = 1
while que:
    i,j = que.popleft()
    for dx,dy in moves:
        x,y = i+dx,j+dy
        if 0<=x<H and 0<=y<W and grid[x][y] == ".":
            if lp[i][j] + 1 > lp[x][y]:
                lp[x][y] = lp[i][j] + 1
                que.append((x,y))
print(max(max(i) for i in lp))