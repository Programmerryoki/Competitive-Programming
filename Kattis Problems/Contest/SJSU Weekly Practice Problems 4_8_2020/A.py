while True:
    N, M = [int(i) for i in input().split()]
    if N == M == 0:
        break

    pos = [[1]*N for i in range(N)]
    for _ in range(M):
        r, c = [int(i) for i in input().split()]
        pos[r][c] = 0

    ans = [[] for _ in range(N)]

    def recur(grid, nq, x, y):
        if nq == N:
            return
        if x == 7:
            return
        i = x+1
        for j in range(N):
            if pos[i][j] == 1 and grid[i][j] == 0 and valid(grid, i, j):
                temp = [[a for a in b] for b in grid]
                temp[i][j] = 1
                if temp not in ans[nq]:
                    # for row in temp:
                    #     print(row)
                    # print()
                    ans[nq].append(temp)
                    recur(temp, nq + 1, i, j)
        # print(nq, x, y)
        # for i in range(x,N):
        #     for j in range(N):
        #         if pos[i][j] == 1 and grid[i][j] == 0 and valid(grid, i, j):
        #             temp = [[a for a in b] for b in grid]
        #             temp[i][j] = 1
        #             if temp not in ans[nq]:
        #                 for row in temp:
        #                     print(row)
        #                 print()
        #                 ans[nq].append(temp)
        #                 recur(temp, nq + 1, i, j)

    def valid(grid, r, c):
        # print(r,c)
        # for row in grid:
        #     print(row)


        if 1 in grid[r]:
            return False
        if 1 in [a[c] for a in grid]:
            return False
        m = min(r, c)
        a = r - m
        b = c - m
        t = min(N-b, N-a)
        # print(r,c,a,b,t)
        # print([grid[a+i][b+i] for i in range(t)])
        if 1 in [grid[a+i][b+i] for i in range(t)]:
            return False

        m = min(N - r - 1, c)
        a = r + m
        b = c - m
        t = a + 1 - b
        # print(r, c, a, b, t, m)
        # print([grid[a - i][b + i] for i in range(t)])
        # print([[a - i,b + i] for i in range(t)])
        if 1 in [grid[a - i][b + i] for i in range(t)]:
            return False
        return True

    t = [[0]*N for i in range(N)]
    recur(t, 0, -1, -1)

    # for q in ans:
    #     for g in q:
    #         for r in g:
    #             print(r)
    #         print()
    print(len(ans[-1]))