from collections import deque

case = 1
while True:
    try:
        m, n = [int(i) for i in input().split()]
    except:
        break

    sky = [input() for i in range(m)]
    seen = set()

    def bfs(a,b):
        que = deque([[a,b]])
        # print(que)
        pos = lambda x,y : [[x-1,y], [x, y-1], [x+1,y], [x,y+1]]
        while len(que) != 0:
            p = que.popleft()
            # print(p)
            i,j = p
            # print(i,j)
            if 0 <= i < m and 0 <= j < n and sky[i][j] == "-" and (i,j) not in seen:
                seen.add((i,j))
                # print(pos(i,j))
                # print(que)
                que += pos(i,j)
                # print(que)

    c = 0
    for i in range(m):
        for j in range(n):
            if sky[i][j] == "-" and (i,j) not in seen:
                bfs(i, j)
                c += 1
    print("Case "+str(case)+":",c)
    case += 1