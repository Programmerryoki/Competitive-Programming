from collections import deque

moves = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs_count(board):
    n = len(board)
    que = deque([(0,0)])
    c = board[0][0]
    seen = {(0,0)}
    edge = set()
    inner = {(0,0)}
    while que:
        i,j = que.popleft()
        for dx,dy in moves:
            x,y = i+dx, j+dy
            if 0<=x<n and 0<=y<n and (x,y) not in seen:
                tup = (x,y)
                if board[x][y] == c:
                    que.append(tup)
                    inner.add(tup)
                else:
                    edge.add(tup)
                seen.add(tup)
    count = [0]*6
    seen = set()
    for e in edge:
        if e in seen:
            continue
        que = deque([e])
        seen.add(e)
        c = board[e[0]][e[1]]
        count[c] += 1
        while que:
            i,j = que.popleft()
            for dx,dy in moves:
                x,y = i+dx, j+dy
                if 0<=x<n and 0<=y<n and (x,y) not in seen and board[x][y] == c:
                    que.append((x,y))
                    count[c] += 1
                    seen.add((x,y))
    # print(count)
    c = count.index(max(count))
    if count[c] == 0:
        return -1
    for i,j in inner:
        board[i][j] = c
    return c

t = int(input())
for _ in range(t):
    n = int(input())
    board = [[int(i)-1 for i in input()] for _ in range(n)]
    colors = [0]*6
    while True:
        # print()
        # for i in board:
        #     print("".join(map(str,i)))
        c = bfs_count(board)
        if c == -1:
            break
        colors[c] += 1
    print(sum(colors))
    print(" ".join(map(str, colors)))