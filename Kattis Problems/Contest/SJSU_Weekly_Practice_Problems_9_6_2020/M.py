P = int(input())
for _ in range(P):
    K,N = [int(i) for i in input().split()]
    board = [0]
    for i in range(N):
        board[0] += 1
        j = 0
        while j < len(board):
            if board[j] > j+1:
                t = board[j]
                if len(board) <= j+1:
                    board.append(0)
                board[j+1] += t - t%(j+2)
                board[j] = t%(j+2)
            j += 1

    print(K,len(board))
    print("\n".join(" ".join(map(str, board[i*10:(i+1)*10])) for i in range((len(board)+9)//10)))