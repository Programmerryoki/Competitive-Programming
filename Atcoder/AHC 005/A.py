# 改善点
#　すべての2編以上周りが開いているマスのみにCを変える
#　Cにあるマスへの最短距離の計算

from sys import stdin
from time import time

moves = {(-1,0):"U", (1,0):"D", (0,-1):"L", (0,1):"R"}
rmoves = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
dircheck = {(-1,0):[(0,-1),(0,1)], (1,0):[(0,-1),(0,1)], (0,-1):[(-1,0),(1,0)], (0,1):[(-1,0),(1,0)]}
order = {(-1,0):0,(1,0):0,(0,-1):1,(0,1):1}
rev = {"U":"D","D":"U","L":"R","R":"L"}

def solve(N,si,sj,C):
    starttime = time()
    parent = {}
    seen = {}
    def dfs(curpos):
        if time() - starttime >= 1:
            raise ConnectionError
        for (dx,dy) in moves:
            tmp = curpos
            check = dircheck[(dx,dy)]
            d = order[(dx,dy)]
            if tmp not in seen:
                seen[tmp] = [0]*2
            while 0 <= tmp[0] < N and 0 <= tmp[1] < N and seen[tmp][d] == 0:
                seen[tmp][d] = 1
                for DX,DY in check:
                    x,y = tmp[0]+DX,tmp[1]+DY
                    dir = order[(DX,DY)]
                    if 0 <= x < N and 0 <= y < N and C[x][y] != "#":
                        tup = (x,y)
                        if tup not in seen:
                            seen[tup] = [0]*2
                        if seen[(x,y)][dir] == 1:
                            continue
                        seen[(x,y)][dir] = 1
                        parent[(x,y)] = curpos
                        dfs(tmp)
                tmp = (tmp[0]+dx,tmp[1]+dy)
                if tmp not in seen:
                    seen[tmp] = [0]*2

    try:
        dfs((si,sj))
    except ConnectionError:
        pass

    best = ""
    score = 0
    for key in parent:
        path = printNonContLst(key, parent, (si,sj))
        c = calcScore(path, C, (si,sj))
        if c > score:
            best = path
            score = c
    # print("Done")
    print(best)

def getmincostList(allpos, C):
    maxl = []
    minc = float("inf")
    for i in allpos:
        cost = getcostList(i, C)
        if i < minc:
            maxl = i
            minc = cost
    return maxl

def getcostList(order, C):
    cost = 0
    for (x,y) in order:
        cost += int(C[x][y])
    return cost

def printAns(poslist):
    cur = poslist[-1]
    ans = ""
    for i in range(1,len(poslist)):
        nxt = poslist[i]
        ans += moves[(cur[0]-nxt[0], cur[1]-nxt[1])]
        cur = nxt
    print(ans)

def printNonContLst(pos, parent, end):
    tmp = pos
    ans = ""
    while tmp != end:
        nxt = parent[tmp]
        dif = [tmp[0]-nxt[0], tmp[1]-nxt[1]]
        if dif[0] != 0:
            ans += ("UD"[dif[0] < 0])*abs(dif[0])
        else:
            ans += ("LR"[dif[1] < 0])*abs(dif[1])
        tmp = nxt
    return "".join(rev[w] for w in ans) + ans

def calcScore(order, C, start):
    # print(order)
    total = len(order)
    cost = 0
    x,y = start
    seen = set(start)
    for i in order:
        cost += int(C[x][y])
        x,y = x+rmoves[i][0], y+rmoves[i][1]
        seen.add((x,y))
    return len(seen) / cost

def main():
    input = stdin.readline
    N,si,sj = [int(i) for i in input().split()]
    C = [input() for i in range(N)]
    solve(N,si,sj,C)

if __name__ == '__main__':
    main()