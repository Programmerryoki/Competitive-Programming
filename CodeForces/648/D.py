from collections import deque
t = int(input())
for _ in range(t):
    n,m = [int(i) for i in input().split()]
    maze = []
    good = []
    bad = []
    for i in range(n):
        line = input()
        for j in range(m):
            if line[j] == "G":
                good.append([i,j])
            elif line[j] == "B":
                bad.append([i,j])
        maze.append(line)
    if len(good) == 0 and len(bad) == 0:
        print("Yes")
        continue

    move = [[1,0],[-1,0],[0,1],[0,-1]]
    gp = [set()]*len(good)
    bp = [set()]*len(bad)
    for num,[i,j] in enumerate(good):
        que = deque([[i,j]])
        path = {}
        seen = {str(i)+" "+str(j)}
        while que:
            node = que.popleft()
            for tx,ty in move:
                x, y = node[0]+tx, node[1]+ty
                pos = str(x)+" "+str(y)
                if 0 <= x < n and 0 <= y < m and pos not in seen and maze[x][y] in {".", "G", "B"}:
                    seen.add(pos)
                    que.append([x,y])
                    path[pos] = str(node[0]) + " " + str(node[1])

        if str(n-1) + " " + str(m-1) in seen:
            node = [n-1,m-1]
            while node != [i,j]:
                s = str(node[0]) + " " + str(node[1])
                gp[num].add(s)
                node = [int(i) for i in path[s].split()]
            gp[num].add(str(node[0]) + " " + str(node[1]))

    for num,[i,j] in enumerate(bad):
        que = deque([[i,j]])
        path = {}
        seen = {str(i)+" "+str(j)}
        while que:
            node = que.popleft()
            for tx,ty in move:
                x, y = node[0]+tx, node[1]+ty
                pos = str(x)+" "+str(y)
                if 0 <= x < n and 0 <= y < m and pos not in seen and maze[x][y] in {".", "G", "B"}:
                    seen.add(pos)
                    que.append([x,y])
                    path[pos] = str(node[0]) + " " + str(node[1])

        if str(n-1) + " " + str(m-1) in seen:
            node = [n-1,m-1]
            while node != [i,j]:
                s = str(node[0]) + " " + str(node[1])
                bp[num].add(s)
                node = [int(i) for i in path[s].split()]
            bp[num].add(str(node[0]) + " " + str(node[1]))

    print(gp)
    print(bp)