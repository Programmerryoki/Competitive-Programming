t = int(input())
for _ in range(t):
    n,m = [int(i) for i in input().split()]
    grid = []
    rgrid = []
    for _ in range(n):
        inp = [int(i) for i in input().split()]
        grid.append(inp)
        rgrid.append(inp[::-1])
    rgrid = rgrid[::-1]
    c = 0
    for i in range(n):
        for j in range(m):
            ri = n - i - 1
            rj = m - j - 1
            if i <= ri and j <= rj:
                if grid[i][j] != grid[ri][rj]:
                    c += 1
    print(c)