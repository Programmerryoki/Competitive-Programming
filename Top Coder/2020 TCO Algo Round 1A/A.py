N = int(input())

grid = []
con = ["X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.",".X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X"]
while 48 < N:
    grid.append(con[0])
    grid.append(con[1])
    grid.append("."*50)
    N -= 48
grid.append(con[0][:N+2])
grid.append(con[1][:N+2])
print(tuple(grid))