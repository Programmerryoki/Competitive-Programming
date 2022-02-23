class UnionFind:
    def __init__(self, N):
        self.N = N
        self.par = [i for i in range(N)]

    def root(self, x):
        if self.par[x] != x:
            self.par[x] = self.root(self.par[x])
        return self.par[x]

    def link(self, x, y):
        rootx = self.root(x)
        rooty = self.root(y)
        if rootx != rooty:
            self.par[y] = rootx

    def connected(self, x, y):
        return self.root(x) == self.root(y)

N = int(input())
Q = int(input())
query = []
for i in range(Q):
    T,X,Y,V = [int(i) for i in input().split()]
    query.append((T,X-1,Y-1,V))
dif = [0]*(N-1)
for T,X,Y,V in query:
    if T == 0:
        dif[X] = V
potential = [0]*N
for i in range(N-1):
    potential[i+1] = dif[i] - potential[i]

uf = UnionFind(N)
for T,X,Y,V in query:
    # print(T,X,Y,V)
    if T == 0:
        uf.link(X, Y)
    else:
        if not uf.connected(X,Y):
            print("Ambiguous")
        elif (X + Y) % 2 == 0:
            print(V + (potential[Y] - potential[X]))
        else:
            print(potential[X] + potential[Y] - V)