class UnionFind:
    def __init__(self):
        self.parent = {}

    def root(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def connect(self,x,y):
        rootx = self.root(x)
        rooty = self.root(y)
        if rootx != rooty:
            if len(rootx) < len(rooty):
                self.parent[rooty] = rootx
            else:
                self.parent[rootx] = rooty

UF = UnionFind()
N,M = [int(i) for i in input().split()]
sentence = input().split()
for _ in range(M):
    w1, w2 = input().split()
    UF.connect(w1, w2)
tn = 0
for i in sentence:
    tn += len(UF.root(i))
print(tn)