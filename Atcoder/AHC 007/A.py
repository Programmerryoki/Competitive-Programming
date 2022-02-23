from sys import stdin
input = stdin.readline
from heapq import heappush, heappop

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
    using = MST(N,M,points,edges,graph)
    for i in range(M):
        length = int(input())
        print(int(i in using), flush=True)

def MST(N,M,points,edges,graph):
    heap = []
    for i,[u,v] in enumerate(edges):
        heappush(heap, [graph[points[u]][points[v]], u, v, i])
    UF = UnionFind()
    edge = set()
    while heap:
        d, u, v, i = heappop(heap)
        if not UF.same(u, v):
            UF.connect(u, v)
            edge.add(i)
    return edge


if __name__ == '__main__':
    main()