board = [input() for i in range(8)]
queen = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == "*":
            queen += 1
            if board[i].count("*") != 1:
                print("invalid")
                exit()
            elif [board[k][j] for k in range(8)].count("*") != 1:
                print("invalid")
                exit()
            pos = [i - min(i,j),j - min(i,j)]
            count = 0
            for k in range(8):
                if board[pos[0]][pos[1]] == "*":
                    count += 1
                pos[0] += 1
                pos[1] += 1
                if not (0 <= pos[0] < 8 and 0 <= pos[1] < 8):
                    break
            if count != 1:
                print("invalid")
                exit()
            pos = [i,j]
            while (0 <= pos[0]+1 < 8 and 0 <= pos[1]-1 < 8):
                pos[0] += 1
                pos[1] -= 1
            # print(pos, [i,j])
            count = 0
            for k in range(8):
                if board[pos[0]][pos[1]] == "*":
                    count += 1
                pos[0] -= 1
                pos[1] += 1
                # print("\t",pos)
                if not (0 <= pos[0] < 8 and 0 <= pos[1] < 8):
                    break
            if count != 1:
                print("invalid")
                exit()
print("valid" if queen == 8 else "invalid")