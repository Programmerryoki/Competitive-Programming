N = int(input())
grid = [[""]*N for i in range(N)]
i = j = 0
dir = [[0,1],[1,0],[0,-1],[-1,0]]
d = 0
num = 1
while num <= N**2:
    grid[i][j] = "0"*(3 - len(str(num))) + str(num)
    if 0 <= i + dir[d][0] < N and 0 <= j + dir[d][1] < N:
        if grid[i+dir[d][0]][j+dir[d][1]] != "":
            d = (d + 1)%len(dir)
    else:
        d = (d + 1)%len(dir)
    i, j = i + dir[d][0], j + dir[d][1]
    num += 1
print("\n".join(" ".join(i) for i in grid))