from collections import deque
n, m = [int(i) for i in input().split()]
grid = [[int(i) for i in input()] for j in range(n)]
mat = [[-1 for i in range(m)] for j in range(n)]
deq = deque()
deq.append((0,0))
mat[0][0] = 0
while mat[n-1][m-1] == -1 and len(deq) != 0:
    r, c = deq.popleft()
    jump = grid[r][c]
    if c + jump < m and mat[r][c+jump] == -1:
        deq.append((r,c+jump))
        mat[r][c+jump] = mat[r][c] + 1
    if c - jump >= 0 and mat[r][c-jump] == -1:
        deq.append((r,c-jump))
        mat[r][c - jump] = mat[r][c] + 1
    if r + jump < n and mat[r+jump][c] == -1:
        deq.append((r+jump,c))
        mat[r + jump][c] = mat[r][c] + 1
    if r - jump >= 0 and mat[r-jump][c] == -1:
        deq.append((r-jump,c))
        mat[r - jump][c] = mat[r][c] + 1
print(mat[n-1][m-1])