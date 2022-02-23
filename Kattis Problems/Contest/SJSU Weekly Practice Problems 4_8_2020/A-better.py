while True:
    N, M = [int(i) for i in input().split()]
    if N == M == 0:
        break

    orow = [0]*N
    ocol = [0]*N
    holes = set(tuple(int(i) for i in input().split()) for j in range(M))
    ans = [[] for i in range(N)]
    q = set()
    count = 0
    def recur(row, col, q, nq):
        global count
        if nq == N:
            count += 1
            return

        for i in range(N):
            if row[i] == 0:
                for j in range(N):
                    if col[j] == 0:
                        if (i, j) not in holes:
                            m = min(i,j)
                            a = i - m
                            b = j - m
                            t = min(N - b, N - a)
                            v = True
                            for k in range(t):
                                if (a+k, b+k) in q:
                                    v = False
                                    break
                            if v:
                                m = min(N-i-1, j)
                                a = i + m
                                b = j - m
                                t = a + 1 - b
                                for k in range(t):
                                    if (a-k, b+k) in q:
                                        v = False
                                        break
                            if v:
                                r = [f for f in row]
                                r[i] += 1
                                c = [f for f in row]
                                c[i] += 1
                                if [r, c] not in ans[nq]:
                                    ans[nq].append([r, c])
                                    recur(r, c, q | {i, j}, nq+1)

    recur(orow, ocol, set(), 0)
    for a in ans:
        print(len(a))
        print(a)
    print(count)