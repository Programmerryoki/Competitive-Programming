from sys import stdin
from time import time
from collections import deque

construct = [(1,0), (0,1)]
moves = {(-1,0):"U", (1,0):"D", (0,-1):"L", (0,1):"R"}
rmoves = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
rev = {"U":"D","D":"U","L":"R","R":"L"}

def calcScore(order, C, start):
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
    graph, pathtonode = dataCleaning(N,si,sj,C)
    # print(pathtonode)
    # print(graph[(si,sj)])
    solve(N,si,sj,C,graph,pathtonode)

def dataCleaning(N, si, sj ,C):
    graph = {}
    edges = lambda pos: sum([(0<=pos[0]+dx<N and 0<=pos[1]+dy<N and C[pos[0]+dx][pos[1]+dy] != "#") for (dx,dy) in moves])
    edgeNum = {}
    pathtonode = {}
    for i in range(N):
        for j in range(N):
            if C[i][j] == "#":
                continue
            pos = (i,j)
            if pos not in edgeNum:
                edgeNum[pos] = edges(pos)
            if edgeNum[pos] < 3:
                continue
            if pos not in graph:
                graph[pos] = {}
            for (dx,dy) in construct:
                tmp = pos
                cost = int(C[i][j])
                while 0<=tmp[0]<N and 0<=tmp[1]<N and C[tmp[0]][tmp[1]] != "#":
                    if tmp == pos:
                        tmp = (tmp[0]+dx,tmp[1]+dy)
                        continue
                    if tmp not in edgeNum:
                        edgeNum[tmp] = edges(tmp)
                    if edges(tmp) >= 3:
                        graph[pos][tmp] = cost
                        if tmp not in graph:
                            graph[tmp] = {}
                        graph[tmp][pos] = cost
                    cost += int(C[tmp[0]][tmp[1]])
                    tmp = (tmp[0]+dx,tmp[1]+dy)
    if (si,sj) not in graph:
        start = (si,sj)
        graph[start] = {}
        que = deque([[0,start]])
        seen = {start}
        parent = {}
        while que:
            cst, node = que.popleft()
            for (dx,dy) in moves:
                x,y = node[0]+dx,node[1]+dy
                if 0<=x<N and 0<=y<N and C[x][y] != "#" and (x,y) not in seen:
                    seen.add((x,y))
                    parent[(x,y)] = node
                    if (x,y) in graph:
                        graph[start][(x,y)] = cst
                        continue
                    que.append([cst+int(C[x][y]),(x,y)])
        for key in graph[start]:
            tmp = key
            path = ""
            while key != start:
                nxt = parent[key]
                d = (key[0]-nxt[0],key[1]-nxt[1])
                path += moves[d]
                key = nxt
            pathtonode[tmp] = path[::-1]
    return graph, pathtonode

def solve(N,si,sj,C,graph,pathtonode):
    starttime = time()

    seen = set()
    best = []
    bestlen = 0
    def dfs(node, order):
        nonlocal seen, best, bestlen
        # if len(order) > bestlen:
        #     best = [order]
        #     bestlen = len(order)
        # elif len(order) == bestlen:
        #     best.append(order)
        if len(order) == len(graph):
            best.append(order)
        if time() - starttime >= 2:
            raise ConnectionError
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                dfs(nxt, order+[nxt])
                seen.remove(nxt)

    try:
        dfs((si,sj), [(si,sj)])
    except ConnectionError:
        pass

    # print(f"{bestlen} out of {len(graph)}")
    bestpath = ""
    score = 0
    for path in best:
        if time() - starttime >= 2.5:
            break
        pathw = printNonContLst(path, pathtonode)
        c = calcScore(pathw, C, (si,sj))
        if c > score:
            bestpath = pathw
            score = c
    print(bestpath)

def printNonContLst(lst, pathtonode):
    ans = ""
    if pathtonode:
        lst = lst[1:]
        ans += pathtonode[lst[0]]
    tmp = lst[0]
    for i in range(1, len(lst)):
        nxt = lst[i]
        dif = [tmp[0]-nxt[0], tmp[1]-nxt[1]]
        if dif[0] != 0:
            ans += ("UD"[dif[0] < 0])*(abs(dif[0]))
        else:
            ans += ("LR"[dif[1] < 0])*(abs(dif[1]))
        tmp = nxt
    return ans + "".join(rev[w] for w in ans[::-1])


if __name__ == '__main__':
    main()