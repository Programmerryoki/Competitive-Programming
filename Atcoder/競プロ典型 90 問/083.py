class unionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]

    def root(self, n):
        if self.par[n] != n:
            self.par[n] = self.root(self.par[n])
        return self.par[n]

    def connect(self, x,n):
        self.root(n)
        self.par[n] = self.root(x)

    def group(self, x):
        return [i for i in range(len(self.par)) if i == x]

N,M = [int(i) for i in input().split()]
color = [0] * N
uf = unionFind(N)
for _ in range(M):
    a,b = [int(i)-1 for i in input().split()]
    uf.connect(a, b)

Q = int(input())
for _ in range(Q):
    x,y = [int(i)-1 for i in input().split()]
    print(color[x]+1)
    for n in uf.group():
        color[n] = y