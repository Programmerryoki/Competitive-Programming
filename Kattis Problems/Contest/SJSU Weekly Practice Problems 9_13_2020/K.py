from collections import deque

N = int(input())
board = [input() for i in range(N)]
K = []
for i in range(N):
    if "K" in board[i]:
        K = [i, board[i].index("K")]
        break

step = [[float("inf")]*N for i in range(N)]
step[K[0]][K[1]] = 0
que = deque([K])
moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
while que:
    i,j = que.popleft()
    for dx,dy in moves:
        x,y = dx+i, dy+j
        if 0 <= x < N and 0 <= y < N and board[x][y] != "#":
            if step[x][y] == float("inf"):
                step[x][y] = step[i][j] + 1
                que.append([x,y])
            if x == y == 0:
                print(step[x][y])
                exit()
print(-1)