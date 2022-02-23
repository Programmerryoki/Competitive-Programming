moves = [[-1,0],[0,1],[1,0],[0,-1]]

T = int(input())
print(T)
for _ in range(T):
    movement = input()
    pos = (0,0)
    dir = 1
    path = [pos]
    for move in movement:
        if move == "F":
            pass
        elif move == "R":
            dir = (dir + 1) % 4
        elif move == "L":
            dir = (dir - 1) % 4
        else:
            dir = (dir + 2) % 4
        x = pos[0] + moves[dir][0]; y = pos[1] + moves[dir][1]
        pos = (x,y)
        path.append(pos)
    mx = [min([i[0] for i in path]),max([i[0] for i in path])]
    my = [min([i[1] for i in path]),max([i[1] for i in path])]

    maze = [["#"]*(my[1]-my[0]+2) for i in range(mx[1]-mx[0]+1)]
    for x,y in path:
        x -= mx[0]; y -= my[0]
        maze[x][y] = "."
    maze = [["#"]*(my[1]-my[0]+2)] + maze + [["#"]*(my[1]-my[0]+2)]

    print(len(maze),len(maze[0]))
    print(*["".join(i) for i in maze],sep="\n")