class SegTree:
    def __init__(self, size):
        n = 1
        while n < size:
            n *= 2
        self.n = n
        self.node = [0]*(2*n)
        self.lazy = [0]*(2*n)

    def eval(self, k):
        sl = self.lazy[k]
        if not sl:
            return
        if k < self.n - 1:
            if sl > self.lazy[2*k+1]:
                self.lazy[2*k+1] = sl
            if sl > self.lazy[2*k+2]:
                self.lazy[2*k+2] = sl
        if sl > self.node[k]:
            self.node[k] = sl
        self.lazy[k] = 0

    def _query(self, a, b, k, l, r):
        self.eval(k)
        if r <= a or b <= 1:
            return 0
        elif a <= l and r <= b:
            return self.node[k]
        elif k < self.n - 1:
            vl = self._query(a, b, k*2+1, l, (l+r) // 2)
            vr = self._query(a, b, k*2+2, (l+r) // 2, r)
            return min(vl, vr)
        return 0

    def query(self, a, b):
        return self._query(a, b, 0, 0, self.n)

    def _update(self, a, b, x, k, l, r):
        self.eval(k)
        if a <= l and r <= b:
            self.lazy[k] = x
            self.eval(k)
        elif a < r and l < b:
            if k < self.n - 1:
                self._update(a, b, x, k*2+1, l, (l+r)//2)
                self._update(a, b, x, k*2+2, (l+r)//2, r)
            self.node[k] = min(self.node[k*2+1], self.node[k*2+2])

    def update(self, a, b, x):
        self._update(a, b, x, 0, 0, self.n)

    def __str__(self):
        return "Node: "+str(self.node) + "\nLazy: " + str(self.lazy)

    def print(self):
        i = 1
        while i <= self.n:
            print(self.node[i:2 * (i)])
            i <<= 1
        print('--------')
        i = 1
        while i <= self.n:
            print(self.lazy[i:2 * (i)])
            i <<= 1
        print()

W,N = [int(i) for i in input().split()]
tree = SegTree(W)
ans = [0]*N
for ind in range(N):
    L,R = [int(i) for i in input().split()]
    h = tree.query(L,R) + 1
    print(L,R+1)
    print(h)
    tree.update(L-1, R, h)
    ans[ind] = h
    print(tree)
    tree.print()
print("\n".join(str(i) for i in ans))