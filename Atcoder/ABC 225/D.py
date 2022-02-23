class UnionFind:
    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(size+1)]
        self.front = [-1]*(size+1)
        self.back = [-1]*(size+1)
        self.history = [[] for _ in range(size+1)]

    def root(self, x):
        if self.parent[x] != x:
            self.history[x].append(self.parent[x])
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def rooth(self, x):
        while not self.same(x, self.parent[x]):
            self.parent[x] = self.history[x].pop()
        return self.parent[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def connect(self, x, y):
        rootx = self.rooth(x)
        rooty = self.rooth(y)
        if rootx != rooty:
            self.parent[rooty] = rootx
            self.front[y] = x
            self.back[x] = y

    def disconnect(self, x, y):
        self.front[y] = -1
        self.back[x] = -1
