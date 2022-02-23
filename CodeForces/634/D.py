t = int(input())
for _ in range(t):
    grid = [list(input()) for i in range(9)]
    grid[0][0] = "1" if grid[0][0] != "1" else "2"
    grid[3][1] = "1" if grid[3][1] != "1" else "2"
    grid[6][2] = "1" if grid[6][2] != "1" else "2"
    grid[1][3] = "1" if grid[1][3] != "1" else "2"
    grid[4][4] = "1" if grid[4][4] != "1" else "2"
    grid[7][5] = "1" if grid[7][5] != "1" else "2"
    grid[2][6] = "1" if grid[2][6] != "1" else "2"
    grid[5][7] = "1" if grid[5][7] != "1" else "2"
    grid[8][8] = "1" if grid[8][8] != "1" else "2"
    print("\n".join("".join(i) for i in grid))