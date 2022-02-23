from sys import stdin
from random import randint, shuffle
from time import time
from copy import deepcopy

def main():
    # Initialize
    input = stdin.readline
    gna = "ABCDEFGH"

    # Getting inputs
    N,M = [int(i) for i in input().split()]
    ans = [["."]*N for i in range(N)]
    words = {}
    ws = [input().strip() for i in range(M)]
    start_time = time()
    def addrest(tmp):
        que = [tmp]
        while que:
            tmp = que.pop()
            for key in tmp:
                tmp[key][1] += 1
                que.append(tmp[key][0])

    for s in ws:
        tmp = words
        for w in s:
            if w in tmp:
                tmp[w][1] += 1
                tmp = tmp[w][0]
            else:
                tmp[w] = [{},1]
                tmp = tmp[w][0]
        if tmp:
            addrest(tmp)
    tmp = []
    def make(dic, w, d):
        nonlocal tmp
        if not dic:
            tmp.append((w,d))
        for key in dic:
            make(dic[key][0], w+key, dic[key][1])
    make(words, "", 0)
    # print(len(tmp))
    shuffle(tmp)
    tmp.sort(key=lambda x:(-x[1],len(x[0])))
    ws = [i[0] for i in tmp if i[1] > 2]
    if len(ws) < 50:
        ws.extend([i[0] for i in tmp if i[1] == 2])
    # print(M,len(tmp), len(ws))
    ws.sort(key=lambda x: len(x))
    # print(tmp)
    # ws[len(ws)//3:] = ws[len(ws)//3:][::-1]

    moves = [(0,1),(1,0)]
    best = 0
    bpos = {}
    so = False
    def recur(ws, pos, used, wd):
        nonlocal best, bpos, so
        # print(wd)
        if time() - start_time > 1.5 + len(ws[0])/10:
            raise ConnectionError
        # elif time() - start_time > 2:
        #     raise ConnectionError
            # and not so:
            # ws[wd:] = sorted(ws[wd:], key=lambda x: (len(x)))
            # so = True
        if wd > best or (wd == best and len(bpos) > len(pos)):
            best = wd
            bpos = deepcopy(pos)
            # print(bpos)

        word = ws[wd]
        s = [(0,0)] if wd == 0 else pos[word[0]] | set([(randint(0,N-1),randint(0,N-1)) for i in range(3)]) | {(randint(0, N-1), 0), (0, randint(0,N-1))}
        for p in s:
            for move in moves:
                check = set((p[0]+move[0]*i,p[1]+move[1]*i) for i in range(len(word)))
                if sum([(0<=i[0]<N) and (0<=i[1]<N) for i in check]) != len(word):
                    continue
                if check & used:
                    continue
                for i in range(len(word)):
                    pos[word[i]].add((p[0]+move[0]*i,p[1]+move[1]*i))
                recur(ws, pos, used | check, wd+1)
                for i in range(len(word)):
                    pos[word[i]].remove((p[0]+move[0]*i,p[1]+move[1]*i))

    try:
        recur(ws, {chr(ord("A")+i):set() for i in range(8)}, set(), 0)
        # print("Done")
    except:
        # print("TLE")
        pass
    for key in bpos:
        for p in bpos[key]:
            ans[p[0]][p[1]] = key
    for i in range(N):
        for j in range(N):
            if ans[i][j] == ".":
                ans[i][j] = gna[randint(0,7)]
    # print(time.time() - start_time)
    print("\n".join("".join(i) for i in ans))
    # print(best)

if __name__ == '__main__':
    main()