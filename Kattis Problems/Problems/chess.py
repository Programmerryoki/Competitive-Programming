n = int(input())

conv = "ABCDEFGH"
move = [[-1,1],[1,1],[1,-1],[-1,-1]]


def dis(a, b):
    return abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2


def movement(dire, pos, end):
    d = 9999
    moving = move[dire]
    larger = False
    while 8 > pos[0]+moving[0] >= 0 and 8 > pos[1]+moving[1] >= 0 and not larger:
        d = dis(pos, end)
        temp = [pos[i] + move[dire][i] for i in range(len(pos))]
        dt = dis(temp, end)
        if d > dt:
            pos = temp.copy()
        else:
            larger = True
        #print(pos, d, dis(pos,end))
    return pos


for i in range(n):
    # Get input and convert all to number
    ax, ay, bx, by = input().split(" ")
    ax, bx = conv.index(ax), conv.index(bx)
    ay, by = int(ay)-1, int(by)-1

    current = [ax, ay]
    end = [bx, by]

    # Check for impossible
    if (ax+ay)%2!=(bx+by)%2:
        print("Impossible")
        continue

    #print("original", current, end)
    grid = [[conv[current[0]], current[1]+1]]
    while dis(current, end) != 0:
        currDis = dis(current, end)
        dire = 0
        while dire < 4:
            temp = [current[i] + move[dire][i] for i in range(len(current))]
            if 0 <= temp[0] < 8 and 0 <= temp[1] < 8 and temp != current:
                if dis(temp, end) < currDis:
                    currDis = dis(current, end)
                    current = movement(dire, current, end)
                    #print(current)
                    if [conv[current[0]], current[1]+1] not in grid:
                        grid.append([conv[current[0]], current[1]+1])
                    if current == end:
                        break
            dire += 1
    #grid.append([conv[end[0]], end[1]+1])
    ans = str(len(grid)-1)
    for j in grid:
        ans += " " + str(j[0]) + " " + str(j[1])
    print(ans)