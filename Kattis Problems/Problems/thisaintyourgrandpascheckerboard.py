n = int(input())
grid = [[1 if i == "B" else 0 for i in input()] for j in range(n)]
valid = True
for a in range(n):
    if sum(grid[a]) != n//2:
        valid = False
        break

    if sum([i[a] for i in grid]) != n//2:
        valid = False

    cc = 0
    cv = 0
    for b in range(n):
        if grid[a][b] == 1:
            cc += 1
            if cc == 3:
                valid = False
                break
        else:
            cc = 0
        if grid[b][a] == 1:
            cv += 1
            if cv == 3:
                valid = False
                break
        else:
            cv = 0
print(int(valid))