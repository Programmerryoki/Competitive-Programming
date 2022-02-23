from sys import stdin
input = stdin.readline
from heapq import heappush, heappop
from time import time

starttime = time()

class UnionFind:
    def __init__(self):
        self.parent = {}

    def root(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def connect(self, x, y):
        rootx, rooty = self.root(x), self.root(y)
        if rootx != rooty:
            self.parent[rootx] = rooty

def main():
    N = 400
    M = 1995
    graph = {}
    points = [tuple([int(i) for i in input().split()]) for _ in range(N)]
    edges = [tuple([int(i) for i in input().split()]) for _ in range(M)]
    for i in range(N):
        graph[points[i]] = {}
    for i in range(M):
        u,v = edges[i]
        d = round(((points[u][0]-points[v][0])**2 + (points[u][1]-points[v][1])**2)**0.5)
        graph[points[u]][points[v]] = d
    solve(N,M,points,edges,graph)

def solve(N,M,points,edges,graph):
    used = set()
    not_used = set()
    using = set()
    tle = False
    for i in range(M):
        length = int(input())
        u,v = edges[i]
        if time() - starttime < 1.7:
            using = MST(N,M,points,edges,graph,used,not_used|{edges[i]})
            if len(using) + len(used) < N-1:
                print(1, flush=True)
                used.add(edges[i])
                continue
            using = MST(N,M,points,edges,graph,used,not_used)
            if length < graph[points[u]][points[v]] * 2:
                print(int(i in using), flush=True)
                if i in using:
                    used.add(edges[i])
                else:
                    not_used.add(edges[i])
            else:
                print(0, flush=True)
                not_used.add(edges[i])
        else:
            if not tle:
                using = MST(N,M,points,edges,graph,used,not_used)
                tle = True
            print(int(i in using), flush=True)

def MST(N,M,points,edges,graph,used,not_used):
    heap = []
    UF = UnionFind()
    for u,v in used:
        UF.connect(u, v)
    for i,(u,v) in enumerate(edges):
        if points[u] in used or points[v] in used or (u,v) in not_used:
            continue
        heappush(heap, [3*graph[points[u]][points[v]], u, v, i])
    edge = set()
    while heap:
        d, u, v, i = heappop(heap)
        if not UF.same(u, v):
            UF.connect(u, v)
            edge.add(i)
    return edge


if __name__ == '__main__':
    main()