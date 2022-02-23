moves = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}

R,C = map(int, input().split())
grid = [input() for i in range(R)]
seen = set()
pos = [0,0]
while True:
    if grid[pos[0]][pos[1]] == "T":
        print(len(seen))
        exit()
    dx,dy = moves[grid[pos[0]][pos[1]]]
    x,y = pos[0]+dx, pos[1]+dy
    if 0 <= x < R and 0 <= y < C:
        if (x,y) in seen:
            print("Lost")
            exit()
        else:
            seen.add((x,y))
            pos = [x,y]
    else:
        print("Out")
        exit()