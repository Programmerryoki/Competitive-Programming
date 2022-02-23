class UnionFind:
    def __init__(self):
        self.parent = {-1:-1}

    def red(self, p):
        self.parent[p] = p

    def root(self, x):
        if x not in self.parent:
            return -1
        stack = []
        t = x
        while t in self.parent and self.parent[t] != t:
            stack.append(t)
            t = self.parent[t]
        for i in range(len(stack)-1, -1, -1):
            self.parent[stack[i]] = t
        return self.parent[x]

    def union(self, x, y):
        rootx = self.root(x)
        rooty = self.root(y)
        if rootx == -1 or rooty == -1:
            return
        if rootx != rooty:
            self.parent[rooty] = rootx

    def same(self, x, y):
        prtx = self.parent[self.root(x)]
        prty = self.parent[self.root(y)]
        return prtx == prty and prtx != -1


H,W = [int(i) for i in input().split()]
Q = int(input())
UF = UnionFind()
moves = [(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(Q):
    q,*rest = [int(i)-1 for i in input().split()]
    if q == 0:
        r,c = rest
        UF.red((r,c))
        for dx,dy in moves:
            x,y = dx+r,dy+c
            if 0 <= x < H and 0 <= y < W:
                UF.union((x,y), (r,c))
    else:
        ra,ca,rb,cb = rest
        print("Yes" if UF.same((ra,ca),(rb,cb)) else "No")