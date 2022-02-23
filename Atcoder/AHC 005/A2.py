from sys import stdin, setrecursionlimit
from time import time
from collections import deque
from heapq import heappop, heappush

setrecursionlimit(10**8)

construct = [(1,0), (0,1)]
moves = {(-1,0):"U", (1,0):"D", (0,-1):"L", (0,1):"R"}
rmoves = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
rev = {"U":"D","D":"U","L":"R","R":"L"}


def main():
    input = stdin.readline
    N,si,sj = [int(i) for i in input().split()]
    C = [input() for i in range(N)]
    graph, pathtonode = dataCleaning(N,si,sj,C)
    graph = genmst(graph, (si,sj))
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

def genmst(graph, start):
    edges = []
    for i in graph[start]:
        heappush(edges, [graph[start][i], start, i])
    mst = {}
    seen = {start}
    while edges:
        cost, n1, n2 = heappop(edges)
        for i in graph[n2]:
            if i in seen:
                continue
            heappush(edges, [graph[n2][i], n2, i])
        if n1 in seen and n2 in seen:
            continue
        seen.add(n1)
        seen.add(n2)
        if n1 not in mst:
            mst[n1] = {}
        if n2 not in mst:
            mst[n2] = {}
        mst[n1][n2] = cost
        mst[n2][n1] = cost
    mst[start] = graph[start]
    return mst

def solve(N,si,sj,C,graph,pathtonode):
    starttime = time()

    que = deque([(si,sj)])
    parent = {}
    seen = {(si,sj)}
    leaf = set()
    while que:
        node = que.popleft()
        for n in graph[node]:
            if n not in seen:
                if node in leaf:
                    leaf.remove(node)
                que.append(n)
                seen.add(n)
                parent[n] = node
                leaf.add(n)

    start = (si,sj)
    tree = {}
    for i in leaf:
        t = []
        tmp = i
        while tmp != start:
            t.append(tmp)
            tmp = parent[tmp]
        path = [start]+t[::-1]
        tmp = tree
        for i in path:
            if i in tmp:
                tmp = tmp[i]
            else:
                tmp[i] = {}
                tmp = tmp[i]
        print(path)
    print(tree)
    path = []
    def dfs(root):
        leaf = True
        for i in root:
            leaf = False
            path.append(i)
            if not dfs(root[i]):
                path.append(i)
        return leaf
    dfs(tree)
    print(path)
    pathw = printNonContLst(path, pathtonode)
    print(calcValid(start, pathw, C))
    print(pathw)

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

def calcValid(start, pathw, C):
    N = len(C)
    x,y = start
    for i in pathw:
        dx,dy = rmoves[i]
        x += dx; y += dy
        if 0<=x<N and 0<=y<N and C[x][y] != "#":
            continue
        print(i)
        return False
    return True

if __name__ == '__main__':
    main()