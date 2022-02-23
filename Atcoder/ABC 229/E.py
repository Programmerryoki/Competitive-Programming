class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.n = size

    def root(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def connect(self, x, y):
        rootx = self.root(x)
        rooty = self.root(y)
        if rootx != rooty:
            self.parent[rooty] = rootx

N,M = [int(i) for i in input().split()]
graph = {i:set() for i in range(N)}
for _ in range(M):
    A,B = [int(i)-1 for i in input().split()]
    graph[A].add(B)
    graph[B].add(A)

UF = UnionFind(N)
ans = [0]*N
d = 0
for i in range(N-1, -1, -1):
    d += 1
    c = 0
    for nxt in graph[i]:
        if nxt < i or UF.same(i, nxt):
            continue
        c += 1
        UF.connect(i, nxt)
    d -= c
    ans[i] = d
print("\n".join(map(str, ans[1:]+[0])))