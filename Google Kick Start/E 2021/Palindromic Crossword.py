from collections import deque

T = int(input())
for case in range(T):
    N,M = [int(i) for i in input().split()]
    grid = [list(input()) for i in range(N)]
    position = {}
    done = set()

    for i in range(N):
        for j in range(M):
            if grid[i][j] == "#":
                continue
            t = (i,j)
            if not (t in position and position[t][0] is not None and position[t][1] is not None):
                # Get the shape of cw
                orii = i
                while 0<i and grid[i-1][j] != "#":
                    i -= 1
                tmp = i
                while i<N-1 and grid[i+1][j] != "#":
                    i += 1
                for k in range(tmp, i+1):
                    tup = (k, j)
                    if tup in position:
                        position[tup][0] = (tmp, i)
                    else:
                        position[tup] = [(tmp,i), None]
                i = orii
                while 0<j and grid[i][j-1] != "#":
                    j -= 1
                tmp = j
                while j<M-1 and grid[i][j+1] != "#":
                    j += 1
                for k in range(tmp, j+1):
                    tup = (i, k)
                    if tup in position:
                        position[tup][1] = (tmp, j)
                    else:
                        position[tup] = [None, (tmp,j)]

    count = 0
    todo = deque()
    for i in range(N):
        for j in range(M):
            if grid[i][j] in ".#":
                continue
            t = (i,j)
            for k in range(2):
                if (t,k) in done:
                    continue
                done.add((t,k))
                start,end = position[t][k]
                rev = end - (t[k] - start)
                rpos = (rev, t[1]) if not k else (t[0], rev)
                if (rpos, k) in done:
                    continue
                done.add((rpos, k))
                if grid[rpos[0]][rpos[1]] == ".":
                    count += 1
                    grid[rpos[0]][rpos[1]] = grid[i][j]
                    if (rpos, 1-k) not in done:
                        todo.append((rpos, 1-k))
    while todo:
        t, k = todo.popleft()
        if (t,k) in done:
            continue
        i,j = t
        done.add((t,k))
        start,end = position[t][k]
        rev = end - (t[k] - start)
        rpos = (rev, t[1]) if not k else (t[0], rev)
        if (rpos, k) in done:
            continue
        done.add((rpos, k))
        if grid[rpos[0]][rpos[1]] == ".":
            count += 1
            grid[rpos[0]][rpos[1]] = grid[i][j]
            if (rpos, 1-k) not in done:
                todo.append((rpos, 1-k))
    print("Case #"+str(case+1)+":",count)
    print("\n".join("".join(i) for i in grid))