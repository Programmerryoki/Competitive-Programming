moves = [[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]

board = [input() for i in range(5)]
count = 0
for i in range(5):
    for j in range(5):
        if board[i][j] != "k":
            continue
        count += 1
        for dx,dy in moves:
            x = dx+i; y = dy+j
            if 0 <= x < 5 and 0 <= y < 5:
                if board[x][y] == "k":
                    print("invalid")
                    exit()
print("valid" if count == 9 else "invalid")