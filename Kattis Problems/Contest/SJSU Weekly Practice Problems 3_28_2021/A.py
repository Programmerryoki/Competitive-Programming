moves = [[-1,0],[0,1],[1,0],[0,-1]]

case = 1
while True:
    W,L = map(int, input().split())
    if W == 0 and L == 0:
        break
    house = [list(input()) for i in range(L)]
    dir = 0
    for i in range(L):
        for j in range(W):
            if house[i][j] == "*":
                pos = [i,j]
                if i == 0:
                    dir = 2
                elif j == 0:
                    dir = 1
                elif j == W-1:
                    dir = 3

    while house[pos[0]][pos[1]] != "x":
        pos[0] += moves[dir][0]
        pos[1] += moves[dir][1]
        hpp = house[pos[0]][pos[1]]
        if hpp == "\\":
            dir = (dir + (1 if dir in [1,3] else -1) + 4) % 4
        elif hpp == "/":
            dir = (dir + (1 if dir in [0,2] else -1) + 4) % 4
    house[pos[0]][pos[1]] = "&"
    print("HOUSE",case)
    print("\n".join("".join(i) for i in house))
    case += 1