board = [list(input()) for i in range(8)]
action = input()
moves = [[-1,0],[0,1],[1,0],[0,-1]]
dir = 1
pos = (7,0)
for act in action:
    if act == "F":
        new = (pos[0]+moves[dir][0],pos[1]+moves[dir][1])
        if (0 <= new[0] < 8 and 0 <= new[1] < 8) and (board[new[0]][new[1]] in "D.T"):
            pos = new
        else:
            print("Bug!")
            exit()
    elif act == "R":
        dir = (dir+1)%4
    elif act == "L":
        dir = (dir+3)%4
    elif act == "X":
        new = (pos[0]+moves[dir][0],pos[1]+moves[dir][1])
        if (0 <= new[0] < 8 and 0 <= new[1] < 8) and (board[new[0]][new[1]] == "I"):
            board[new[0]][new[1]] = "."
        else:
            print("Bug!")
            exit()
print("Diamond!" if board[pos[0]][pos[1]] == "D" else "Bug!")