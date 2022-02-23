grid = [input().split() for i in range(6)]
missr = [[] for i in range(6)]
missc = [[] for i in range(6)]
for i,row in enumerate(grid):
    val = [1]*9
    for j,col in enumerate(row):
        if len(col.split("/")) == 1:
            n = int(col)
            val[n-1] = 0
            grid[i][j] = n
        else:
            n1 = int(col[0])
            n2 = int(col[-1])
            val[n1-1] = 0
            val[n2-1] = 0
            grid[i][j] = [n1, n2]
