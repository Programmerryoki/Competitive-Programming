from heapq import heapify, heappop
from sys import stdin
input = stdin.readline

class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]

    def root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        rootx = self.root(x); rooty = self.root(y)
        if rootx != rooty:
            self.parent[rooty] = rootx

def main():
    N,M,Q = [int(i) for i in input().split()]
    UF = UnionFind(N)
    edges = []
    for _ in range(M):
        a,b,c = [int(i) for i in input().split()]
        edges.append([c,1,a-1,b-1])
    for i in range(Q):
        u,v,w = [int(i) for i in input().split()]
        edges.append([w,-i,u-1,v-1])
    heapify(edges)
    ne = 0
    ans = ["No"]*Q
    while edges:
        c,ind,a,b = heappop(edges)
        if ind == 1:
            UF.union(a,b)
            ne += 1
        elif not UF.same(a,b):
            ans[-ind] = "Yes"
    print("\n".join(ans))

if __name__ == '__main__':
    main()

#
# order = []
# def cycle(cur):
#     global order
#
#
# N,M,Q = [int(i) for i in input().split()]
# edges = []
# for _ in range(M):
#     a,b,c = [int(i) for i in input().split()]
#     edges.append([c, a-1, b-1])
# heapify(edges)
# mst = {i:{} for i in range(N)}
# used = set()
# UF = UnionFind(N)
# while edges:
#     c, a, b = heappop(edges)
#     if UF.same(a,b):
#         continue
#     mst[a][b] = c
#     mst[b][a] = c
#     UF.union(a,b)
#
# for _ in range(Q):
#     u,v,w = [int(i) for i in input().split()]
#     if v in mst[u]:
#         print("Yes" if w <= mst[u][v] else "No")
#         continue
#     mst[u][v] = w
#     mst[v][u] = w
